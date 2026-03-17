from pathlib import Path

from mutation_tool.config import load_config
from mutation_tool.discovery import discover_python_files


def test_discovery_excludes_tests_directory(tmp_path: Path) -> None:
    source_dir = tmp_path / "src"
    source_dir.mkdir(parents=True)
    (source_dir / "app.py").write_text("print('x')\n", encoding="utf-8")

    tests_dir = tmp_path / "tests"
    tests_dir.mkdir()
    (tests_dir / "test_app.py").write_text("def test_ok():\n    assert True\n", encoding="utf-8")

    config = load_config(tmp_path)
    discovered = discover_python_files(config)

    assert discovered == [source_dir / "app.py"]
