from __future__ import annotations

import subprocess
import time
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class CommandResult:
    exit_code: int
    stdout: str
    stderr: str
    duration_seconds: float
    timed_out: bool


def run_command(cwd: Path, command: list[str], timeout: float | None) -> CommandResult:
    started = time.perf_counter()
    try:
        completed = subprocess.run(
            command,
            cwd=cwd,
            check=False,
            capture_output=True,
            text=True,
            timeout=timeout,
        )
        duration = time.perf_counter() - started
        return CommandResult(
            exit_code=completed.returncode,
            stdout=completed.stdout,
            stderr=completed.stderr,
            duration_seconds=duration,
            timed_out=False,
        )
    except subprocess.TimeoutExpired as exc:
        duration = time.perf_counter() - started
        return CommandResult(
            exit_code=124,
            stdout=_decode_timeout_stream(exc.stdout),
            stderr=_decode_timeout_stream(exc.stderr),
            duration_seconds=duration,
            timed_out=True,
        )


def extract_failure_summary(output: str) -> str | None:
    lines = [line.strip() for line in output.splitlines() if line.strip()]
    summary_lines = [line for line in lines if "FAILED" in line or "ERROR" in line]
    if summary_lines:
        return " | ".join(summary_lines[:3])
    return None


def looks_like_error(output: str) -> bool:
    error_markers = (
        "SyntaxError",
        "IndentationError",
        "ERROR collecting",
        "ModuleNotFoundError",
        "ImportError",
    )
    return any(marker in output for marker in error_markers)


def _decode_timeout_stream(payload: str | bytes | None) -> str:
    if payload is None:
        return ""
    if isinstance(payload, bytes):
        return payload.decode("utf-8", errors="replace")
    return payload
