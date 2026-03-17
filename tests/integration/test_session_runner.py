from pathlib import Path

from mutation_tool.config import load_config
from mutation_tool.engine.session import SessionRunner
from mutation_tool.models import MutantStatus


def test_session_runner_kills_detected_mutant() -> None:
    project_root = Path("tests/integration/fixtures/killed_project").resolve()

    session = SessionRunner(load_config(project_root)).run()

    assert session.baseline.success is True
    assert session.generated_mutants == 1
    assert [result.status for result in session.mutants] == [MutantStatus.KILLED]


def test_session_runner_reports_survivor() -> None:
    project_root = Path("tests/integration/fixtures/survivor_project").resolve()

    session = SessionRunner(load_config(project_root)).run()

    assert session.baseline.success is True
    assert session.generated_mutants == 1
    assert [result.status for result in session.mutants] == [MutantStatus.SURVIVED]
