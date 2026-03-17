from __future__ import annotations

from mutation_tool.discovery import discover_python_files
from mutation_tool.engine.baseline import resolve_mutant_timeout, run_baseline
from mutation_tool.engine.generator import generate_mutations
from mutation_tool.engine.runner import (
    extract_failure_summary,
    looks_like_error,
    run_command,
)
from mutation_tool.engine.workspace import prepare_workspace
from mutation_tool.models import (
    MutantResult,
    MutantStatus,
    MutationSpec,
    SessionResult,
    ToolConfig,
)
from mutation_tool.operators import MutationOperator, build_default_operators


class SessionRunner:
    def __init__(self, config: ToolConfig) -> None:
        self.config = config
        self.operators = self._resolve_operators(config.enabled_operators)

    def run(self) -> SessionResult:
        discovered_files = discover_python_files(self.config)
        baseline = run_baseline(self.config)
        session = SessionResult(
            config=self.config,
            baseline=baseline,
            discovered_files=discovered_files,
        )
        if not baseline.success:
            return session

        mutations = generate_mutations(discovered_files, self.config.project_root, self.operators)
        if self.config.max_mutants is not None:
            mutations = mutations[: self.config.max_mutants]
        session.generated_mutants = len(mutations)

        timeout_seconds = resolve_mutant_timeout(self.config, baseline.duration_seconds)
        for mutation in mutations:
            result = self._run_mutation(mutation, timeout_seconds)
            session.mutants.append(result)
            if self.config.stop_on_survivor and result.status is MutantStatus.SURVIVED:
                break
        return session

    def _run_mutation(self, spec: MutationSpec, timeout_seconds: float) -> MutantResult:
        temporary_directory, workspace_root = prepare_workspace(self.config, spec)
        try:
            command_result = run_command(workspace_root, self.config.test_command, timeout_seconds)
        finally:
            temporary_directory.cleanup()

        output = f"{command_result.stdout}\n{command_result.stderr}"
        if command_result.timed_out:
            status = MutantStatus.TIMEOUT
        elif command_result.exit_code == 0:
            status = MutantStatus.SURVIVED
        elif looks_like_error(output):
            status = MutantStatus.ERROR
        else:
            status = MutantStatus.KILLED

        return MutantResult(
            spec=spec,
            status=status,
            duration_seconds=command_result.duration_seconds,
            exit_code=command_result.exit_code,
            stdout=command_result.stdout,
            stderr=command_result.stderr,
            timeout_seconds=timeout_seconds,
            failing_summary=extract_failure_summary(output),
        )

    def _resolve_operators(self, enabled_names: list[str]) -> list[MutationOperator]:
        available = {operator.name: operator for operator in build_default_operators()}
        if not enabled_names:
            return list(available.values())
        missing = [name for name in enabled_names if name not in available]
        if missing:
            available_names = ", ".join(sorted(available))
            missing_names = ", ".join(missing)
            raise ValueError(f"Unknown operator(s): {missing_names}. Available: {available_names}")
        return [available[name] for name in enabled_names]
