from __future__ import annotations

from pathlib import Path

from mutation_tool.models import ToolConfig


def discover_python_files(config: ToolConfig) -> list[Path]:
    discovered: list[Path] = []
    for source_path in config.source_paths:
        if not source_path.exists():
            continue
        if source_path.is_file() and source_path.suffix == ".py":
            if not should_exclude(source_path, config):
                discovered.append(source_path.resolve())
            continue
        for candidate in sorted(source_path.rglob("*.py")):
            if not should_exclude(candidate, config):
                discovered.append(candidate.resolve())
    return _deduplicate(discovered)


def should_exclude(path: Path, config: ToolConfig) -> bool:
    if any(part in {"__pycache__", ".git", ".venv", "venv"} for part in path.parts):
        return True

    try:
        relative = path.resolve().relative_to(config.project_root)
    except ValueError:
        return True

    relative_posix = relative.as_posix()
    for pattern in config.exclude:
        normalized = pattern.replace("\\", "/")
        if relative.match(normalized) or _glob_matches(relative_posix, normalized):
            return True
    return False


def _glob_matches(relative_path: str, pattern: str) -> bool:
    if pattern.startswith("**/"):
        return Path(relative_path).match(pattern[3:]) or Path(relative_path).match(pattern)
    return Path(relative_path).match(pattern)


def _deduplicate(paths: list[Path]) -> list[Path]:
    seen: set[Path] = set()
    result: list[Path] = []
    for path in paths:
        if path not in seen:
            result.append(path)
            seen.add(path)
    return result
