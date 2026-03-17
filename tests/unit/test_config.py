import sys
from pathlib import Path

import pytest

from mutation_tool.config import load_config


def test_load_config_reads_tool_section(tmp_path: Path) -> None:
    (tmp_path / "pyproject.toml").write_text(
        """
[tool.mutation_tool]
source_paths = ["app"]
test_command = ["pytest", "-q", "tests"]
exclude = ["generated/**"]
timeout_multiplier = 3.0
min_timeout = 2.5
max_mutants = 10
stop_on_survivor = true
""".strip(),
        encoding="utf-8",
    )

    config = load_config(tmp_path)

    assert config.source_paths == [tmp_path / "app"]
    assert config.test_command == [sys.executable, "-m", "pytest", "-q", "tests"]
    assert "generated/**" in config.exclude
    assert config.timeout_multiplier == 3.0
    assert config.min_timeout == 2.5
    assert config.max_mutants == 10
    assert config.stop_on_survivor is True


def test_load_config_uses_defaults_when_missing(tmp_path: Path) -> None:
    config = load_config(tmp_path)

    assert config.source_paths == [tmp_path / "src"]
    assert config.test_command == [sys.executable, "-m", "pytest", "-q"]
    assert config.report_dir == tmp_path / ".mutation-tool"


def test_load_config_rejects_boolean_for_numeric_fields(tmp_path: Path) -> None:
    (tmp_path / "pyproject.toml").write_text(
        """
[tool.mutation_tool]
max_mutants = true
""".strip(),
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="Expected an integer or string value"):
        load_config(tmp_path)
