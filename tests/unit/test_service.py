from pathlib import Path

import pytest

from mutation_tool.config import load_config
from mutation_tool.engine.session import SessionRunner
from mutation_tool.service import RunOptions, build_runtime_config, execute_session


def test_build_runtime_config_rejects_missing_source_paths(tmp_path: Path) -> None:
    (tmp_path / "pyproject.toml").write_text(
        """
[tool.mutation_tool]
source_paths = ["missing"]
""".strip(),
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="None of the configured source paths exist"):
        build_runtime_config(RunOptions(project_root=tmp_path))


def test_session_runner_requires_discoverable_python_files(tmp_path: Path) -> None:
    source_dir = tmp_path / "src"
    source_dir.mkdir(parents=True)

    config = load_config(tmp_path)

    with pytest.raises(
        ValueError,
        match="No Python source files matched the configured source paths and exclude patterns",
    ):
        SessionRunner(config).run()


def test_execute_session_writes_json_and_pdf_reports() -> None:
    project_root = Path("tests/integration/fixtures/killed_project").resolve()

    result = execute_session(load_config(project_root))

    assert result.json_report_path.exists() is True
    assert result.json_report_path.name == "last-run.json"
    assert result.pdf_report_path.exists() is True
    assert result.pdf_report_path.name == "last-run.pdf"
