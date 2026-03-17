from __future__ import annotations

from dataclasses import dataclass, replace
from pathlib import Path

from mutation_tool.config import load_config
from mutation_tool.engine.session import SessionRunner
from mutation_tool.models import SessionResult, ToolConfig
from mutation_tool.reports import write_json_report
from mutation_tool.storage import ensure_directory


@dataclass(frozen=True)
class RunOptions:
    project_root: Path
    config_path: Path | None = None
    source_paths: tuple[Path, ...] = ()
    operators: tuple[str, ...] = ()
    max_mutants: int | None = None
    per_mutant_timeout: float | None = None
    fail_on_survivor: bool | None = None


@dataclass(frozen=True)
class ExecutionResult:
    session: SessionResult
    report_path: Path


def build_runtime_config(options: RunOptions) -> ToolConfig:
    project_root = options.project_root.resolve()
    if not project_root.exists() or not project_root.is_dir():
        raise ValueError(f"Project root does not exist or is not a directory: {project_root}")

    config_path = options.config_path.resolve() if options.config_path is not None else None
    config = load_config(project_root, config_path)

    if options.source_paths:
        resolved_sources = [
            _resolve_project_path(project_root, path) for path in options.source_paths
        ]
        config = replace(config, source_paths=resolved_sources)
    if options.operators:
        config = replace(config, enabled_operators=list(options.operators))
    if options.max_mutants is not None:
        config = replace(config, max_mutants=options.max_mutants)
    if options.per_mutant_timeout is not None:
        config = replace(config, per_mutant_timeout=options.per_mutant_timeout)
    if options.fail_on_survivor is not None:
        config = replace(config, fail_on_survivor=options.fail_on_survivor)
    return config


def execute_options(options: RunOptions) -> ExecutionResult:
    return execute_session(build_runtime_config(options))


def execute_session(config: ToolConfig) -> ExecutionResult:
    session = SessionRunner(config).run()
    report_dir = ensure_directory(config.report_dir)
    report_path = write_json_report(session, report_dir / "last-run.json")
    return ExecutionResult(session=session, report_path=report_path)


def _resolve_project_path(project_root: Path, value: Path) -> Path:
    if value.is_absolute():
        return value.resolve()
    return (project_root / value).resolve()
