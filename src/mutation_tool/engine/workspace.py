from __future__ import annotations

import shutil
from pathlib import Path
from tempfile import TemporaryDirectory

from mutation_tool.engine.generator import apply_mutation_to_source
from mutation_tool.models import MutationSpec, ToolConfig


def prepare_workspace(
    config: ToolConfig,
    spec: MutationSpec,
) -> tuple[TemporaryDirectory[str], Path]:
    temporary_directory = TemporaryDirectory(prefix="mutation-tool-")
    workspace_root = Path(temporary_directory.name) / config.project_root.name
    shutil.copytree(
        config.project_root,
        workspace_root,
        ignore=shutil.ignore_patterns(
            ".git",
            "__pycache__",
            ".pytest_cache",
            ".mypy_cache",
            ".ruff_cache",
            ".venv",
            "venv",
            config.report_dir.name,
        ),
    )

    target_file = workspace_root / spec.file_path
    source = target_file.read_text(encoding="utf-8")
    target_file.write_text(apply_mutation_to_source(source, spec), encoding="utf-8")
    return temporary_directory, workspace_root
