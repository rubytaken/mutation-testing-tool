from __future__ import annotations

from mutation_tool.engine.runner import run_command
from mutation_tool.models import BaselineResult, ToolConfig


def run_baseline(config: ToolConfig) -> BaselineResult:
    result = run_command(
        cwd=config.project_root,
        command=config.test_command,
        timeout=config.baseline_timeout,
    )
    return BaselineResult(
        success=(not result.timed_out and result.exit_code == 0),
        duration_seconds=result.duration_seconds,
        exit_code=result.exit_code,
        stdout=result.stdout,
        stderr=result.stderr,
        command=config.test_command,
    )


def resolve_mutant_timeout(config: ToolConfig, baseline_duration: float) -> float:
    if config.per_mutant_timeout is not None:
        return config.per_mutant_timeout
    return max(config.min_timeout, baseline_duration * config.timeout_multiplier)
