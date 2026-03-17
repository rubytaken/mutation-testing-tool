from pathlib import Path

from typer.testing import CliRunner

from mutation_tool.cli import app


def test_list_operators_command() -> None:
    runner = CliRunner()
    result = runner.invoke(app, ["list-operators"])

    assert result.exit_code == 0
    assert "comparison" in result.stdout


def test_run_command_writes_json_report() -> None:
    project_root = Path("tests/integration/fixtures/killed_project").resolve()
    runner = CliRunner()

    result = runner.invoke(app, ["run", str(project_root), "--max-mutants", "1"])

    assert result.exit_code == 0
    assert (project_root / ".mutation-tool" / "last-run.json").exists()


def test_ui_command_help() -> None:
    runner = CliRunner()

    result = runner.invoke(app, ["ui", "--help"])

    assert result.exit_code == 0
    assert "--host" in result.stdout
