from __future__ import annotations

import sys
import tomllib
from pathlib import Path
from typing import cast

from mutation_tool.models import ToolConfig

DEFAULT_SOURCE_PATHS = ["src"]
DEFAULT_TEST_COMMAND = ["pytest", "-q"]
DEFAULT_EXCLUDE = [
    "tests/**",
    "test/**",
    "**/__pycache__/**",
    "**/.pytest_cache/**",
    "**/.mypy_cache/**",
    "**/.ruff_cache/**",
    "**/.venv/**",
    "**/venv/**",
    "**/.git/**",
]
DEFAULT_REPORT_DIR = ".mutation-tool"


def load_config(project_root: Path, config_path: Path | None = None) -> ToolConfig:
    project_root = project_root.resolve()
    config_file = _resolve_config_path(project_root, config_path)
    raw_config = _read_tool_section(config_file) if config_file else {}

    configured_sources = _as_string_list(raw_config.get("source_paths"))
    source_paths = [project_root / value for value in configured_sources]
    if not source_paths:
        source_paths = [project_root / value for value in DEFAULT_SOURCE_PATHS]

    test_command = _normalize_test_command(
        _as_string_list(raw_config.get("test_command")) or list(DEFAULT_TEST_COMMAND)
    )
    exclude = _merge_unique(DEFAULT_EXCLUDE, _as_string_list(raw_config.get("exclude")))
    enabled_operators = _as_string_list(raw_config.get("operators"))

    report_dir_value = raw_config.get("report_dir", DEFAULT_REPORT_DIR)
    report_dir = project_root / str(report_dir_value)

    return ToolConfig(
        project_root=project_root,
        source_paths=source_paths,
        test_command=test_command,
        exclude=exclude,
        enabled_operators=enabled_operators,
        timeout_multiplier=_as_float(raw_config.get("timeout_multiplier", 5.0)),
        min_timeout=_as_float(raw_config.get("min_timeout", 5.0)),
        baseline_timeout=_as_optional_float(raw_config.get("baseline_timeout")),
        per_mutant_timeout=_as_optional_float(raw_config.get("per_mutant_timeout")),
        report_dir=report_dir,
        max_mutants=_as_optional_int(raw_config.get("max_mutants")),
        stop_on_survivor=bool(raw_config.get("stop_on_survivor", False)),
        fail_on_survivor=bool(raw_config.get("fail_on_survivor", False)),
    )


def _resolve_config_path(project_root: Path, config_path: Path | None) -> Path | None:
    if config_path is not None:
        return config_path.resolve()
    candidate = project_root / "pyproject.toml"
    return candidate if candidate.exists() else None


def _read_tool_section(config_file: Path) -> dict[str, object]:
    with config_file.open("rb") as handle:
        data = tomllib.load(handle)
    tool_section = data.get("tool", {})
    if not isinstance(tool_section, dict):
        return {}
    mutation_section = tool_section.get("mutation_tool", {})
    if not isinstance(mutation_section, dict):
        return {}
    return cast(dict[str, object], mutation_section)


def _as_string_list(value: object) -> list[str]:
    if value is None:
        return []
    if isinstance(value, str):
        return [value]
    if isinstance(value, list) and all(isinstance(item, str) for item in value):
        return list(value)
    raise ValueError("Expected a string or list of strings in mutation tool config")


def _as_optional_float(value: object) -> float | None:
    if value is None:
        return None
    if isinstance(value, bool):
        raise ValueError("Expected a numeric or string value in mutation tool config")
    if not isinstance(value, int | float | str):
        raise ValueError("Expected a numeric or string value in mutation tool config")
    return float(value)


def _as_float(value: object) -> float:
    converted = _as_optional_float(value)
    if converted is None:
        raise ValueError("Expected a numeric value in mutation tool config")
    return converted


def _as_optional_int(value: object) -> int | None:
    if value is None:
        return None
    if isinstance(value, bool):
        raise ValueError("Expected an integer or string value in mutation tool config")
    if not isinstance(value, int | str):
        raise ValueError("Expected an integer or string value in mutation tool config")
    return int(value)


def _normalize_test_command(command: list[str]) -> list[str]:
    if command and command[0] == "pytest":
        return [sys.executable, "-m", "pytest", *command[1:]]
    return command


def _merge_unique(left: list[str], right: list[str]) -> list[str]:
    merged: list[str] = []
    for item in [*left, *right]:
        if item not in merged:
            merged.append(item)
    return merged
