from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from threading import Lock, Thread

from mutation_tool.operators import build_default_operators
from mutation_tool.reports import session_to_dict
from mutation_tool.service import ExecutionResult, RunOptions, execute_options

type Executor = Callable[[RunOptions], ExecutionResult]


@dataclass(frozen=True)
class RunRequest:
    project_root: str
    config_path: str | None = None
    source_paths: tuple[str, ...] = ()
    operators: tuple[str, ...] = ()
    max_mutants: int | None = None
    per_mutant_timeout: float | None = None
    fail_on_survivor: bool | None = None

    def to_options(self) -> RunOptions:
        return RunOptions(
            project_root=_to_path(self.project_root),
            config_path=_to_optional_path(self.config_path),
            source_paths=tuple(_to_path(path) for path in self.source_paths),
            operators=self.operators,
            max_mutants=self.max_mutants,
            per_mutant_timeout=self.per_mutant_timeout,
            fail_on_survivor=self.fail_on_survivor,
        )

    def to_dict(self) -> dict[str, object]:
        return {
            "project_root": self.project_root,
            "config_path": self.config_path,
            "source_paths": list(self.source_paths),
            "operators": list(self.operators),
            "max_mutants": self.max_mutants,
            "per_mutant_timeout": self.per_mutant_timeout,
            "fail_on_survivor": self.fail_on_survivor,
        }


@dataclass
class RunSnapshot:
    status: str = "idle"
    message: str = "Ready to launch mutation analysis."
    started_at: str | None = None
    finished_at: str | None = None
    report_path: str | None = None
    error: str | None = None
    request: dict[str, object] | None = None
    result: dict[str, object] | None = None

    def to_dict(self) -> dict[str, object]:
        return {
            "status": self.status,
            "message": self.message,
            "started_at": self.started_at,
            "finished_at": self.finished_at,
            "report_path": self.report_path,
            "error": self.error,
            "request": self.request,
            "result": self.result,
        }


class UIState:
    def __init__(self, executor: Executor | None = None) -> None:
        self._executor = executor or execute_options
        self._lock = Lock()
        self._snapshot = RunSnapshot()
        self._operator_names = [operator.name for operator in build_default_operators()]

    def available_operators(self) -> list[str]:
        return list(self._operator_names)

    def snapshot(self) -> dict[str, object]:
        with self._lock:
            return self._snapshot.to_dict()

    def start_run(self, request: RunRequest) -> dict[str, object]:
        with self._lock:
            if self._snapshot.status == "running":
                raise RuntimeError("A mutation run is already in progress.")
            self._snapshot = RunSnapshot(
                status="running",
                message="Mutation analysis is running.",
                started_at=_timestamp(),
                request=request.to_dict(),
            )

        worker = Thread(target=self._finish_run, args=(request,), daemon=True)
        worker.start()
        return self.snapshot()

    def run_blocking(self, request: RunRequest) -> dict[str, object]:
        with self._lock:
            self._snapshot = RunSnapshot(
                status="running",
                message="Mutation analysis is running.",
                started_at=_timestamp(),
                request=request.to_dict(),
            )
        self._finish_run(request)
        return self.snapshot()

    def _finish_run(self, request: RunRequest) -> None:
        started_at = self._started_at()
        try:
            execution = self._executor(request.to_options())
            snapshot = RunSnapshot(
                status="completed",
                message="Mutation analysis completed.",
                started_at=started_at,
                finished_at=_timestamp(),
                report_path=str(execution.report_path),
                request=request.to_dict(),
                result=session_to_dict(execution.session, execution.report_path),
            )
        except Exception as exc:
            snapshot = RunSnapshot(
                status="failed",
                message="Mutation analysis failed.",
                started_at=started_at,
                finished_at=_timestamp(),
                error=str(exc),
                request=request.to_dict(),
            )

        with self._lock:
            self._snapshot = snapshot

    def _started_at(self) -> str | None:
        with self._lock:
            return self._snapshot.started_at


def _timestamp() -> str:
    return datetime.now(UTC).isoformat()


def _to_path(value: str) -> Path:
    return Path(value)


def _to_optional_path(value: str | None) -> Path | None:
    if value is None or not value.strip():
        return None
    return _to_path(value)
