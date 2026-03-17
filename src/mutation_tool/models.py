from __future__ import annotations

from dataclasses import dataclass, field
from enum import StrEnum
from pathlib import Path


class MutantStatus(StrEnum):
    KILLED = "killed"
    SURVIVED = "survived"
    TIMEOUT = "timeout"
    ERROR = "error"


@dataclass(frozen=True)
class MutationLocation:
    start_line: int
    start_col: int
    end_line: int
    end_col: int


@dataclass(frozen=True)
class MutationSpec:
    mutant_id: str
    file_path: Path
    operator_name: str
    location: MutationLocation
    original_snippet: str
    mutated_snippet: str
    description: str


@dataclass(frozen=True)
class ToolConfig:
    project_root: Path
    source_paths: list[Path]
    test_command: list[str]
    exclude: list[str]
    enabled_operators: list[str]
    timeout_multiplier: float
    min_timeout: float
    baseline_timeout: float | None
    per_mutant_timeout: float | None
    report_dir: Path
    max_mutants: int | None = None
    stop_on_survivor: bool = False
    fail_on_survivor: bool = False


@dataclass(frozen=True)
class BaselineResult:
    success: bool
    duration_seconds: float
    exit_code: int
    stdout: str
    stderr: str
    command: list[str]


@dataclass(frozen=True)
class MutantResult:
    spec: MutationSpec
    status: MutantStatus
    duration_seconds: float
    exit_code: int
    stdout: str
    stderr: str
    timeout_seconds: float
    failing_summary: str | None = None


@dataclass
class SessionResult:
    config: ToolConfig
    baseline: BaselineResult
    mutants: list[MutantResult] = field(default_factory=list)
    discovered_files: list[Path] = field(default_factory=list)
    generated_mutants: int = 0

    @property
    def killed(self) -> int:
        return sum(result.status is MutantStatus.KILLED for result in self.mutants)

    @property
    def survived(self) -> int:
        return sum(result.status is MutantStatus.SURVIVED for result in self.mutants)

    @property
    def timed_out(self) -> int:
        return sum(result.status is MutantStatus.TIMEOUT for result in self.mutants)

    @property
    def errors(self) -> int:
        return sum(result.status is MutantStatus.ERROR for result in self.mutants)

    @property
    def executed(self) -> int:
        return len(self.mutants)

    @property
    def mutation_score(self) -> float:
        relevant = self.killed + self.survived
        if relevant == 0:
            return 0.0
        return (self.killed / relevant) * 100.0
