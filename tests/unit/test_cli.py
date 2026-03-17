from pathlib import Path

import pytest
from typer.testing import CliRunner

from mutation_tool.cli import app
from mutation_tool.models import BaselineResult, SessionResult, ToolConfig
from mutation_tool.service import ExecutionResult, RunOptions


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


def test_run_command_passes_stop_on_survivor_option(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    captured: list[RunOptions] = []
    project_root = Path("tests/integration/fixtures/killed_project").resolve()

    def fake_execute_options(options: RunOptions) -> ExecutionResult:
        captured.append(options)
        config = ToolConfig(
            project_root=project_root,
            source_paths=[project_root / "src"],
            test_command=["python", "-m", "pytest", "-q"],
            exclude=[],
            enabled_operators=[],
            timeout_multiplier=5.0,
            min_timeout=5.0,
            baseline_timeout=None,
            per_mutant_timeout=None,
            report_dir=project_root / ".mutation-tool",
        )
        session = SessionResult(
            config=config,
            baseline=BaselineResult(
                success=True,
                duration_seconds=0.1,
                exit_code=0,
                stdout="",
                stderr="",
                command=config.test_command,
            ),
        )
        return ExecutionResult(
            session=session,
            report_path=project_root / ".mutation-tool" / "stub.json",
        )

    monkeypatch.setattr("mutation_tool.cli.execute_options", fake_execute_options)

    runner = CliRunner()
    result = runner.invoke(
        app,
        ["run", str(project_root), "--stop-on-survivor"],
    )

    assert result.exit_code == 0
    assert captured
    assert captured[0].stop_on_survivor is True
