from __future__ import annotations

from pathlib import Path

from fastapi.testclient import TestClient

from mutation_tool.config import load_config
from mutation_tool.engine.session import SessionRunner
from mutation_tool.service import ExecutionResult, RunOptions
from mutation_tool.ui.app import create_app
from mutation_tool.ui.state import RunRequest, UIState


class StubState:
    def __init__(self) -> None:
        self.started_request: RunRequest | None = None

    def available_operators(self) -> list[str]:
        return ["comparison", "logical"]

    def snapshot(self) -> dict[str, object]:
        return {"status": "idle", "message": "Ready", "result": None}

    def start_run(self, request: RunRequest) -> dict[str, object]:
        self.started_request = request
        return {
            "status": "running",
            "message": "Mutation analysis is running.",
            "request": request.to_dict(),
            "result": None,
        }


def test_ui_index_page_loads() -> None:
    client = TestClient(create_app(StubState()))

    response = client.get("/")

    assert response.status_code == 200
    assert "Mutation Lab" in response.text


def test_ui_exposes_operator_list() -> None:
    client = TestClient(create_app(StubState()))

    response = client.get("/api/operators")

    assert response.status_code == 200
    assert response.json() == {"operators": ["comparison", "logical"]}


def test_ui_run_endpoint_accepts_payload() -> None:
    state = StubState()
    client = TestClient(create_app(state))

    response = client.post(
        "/api/run",
        json={
            "project_root": ".",
            "source_paths": ["src"],
            "operators": ["comparison"],
            "max_mutants": 5,
        },
    )

    assert response.status_code == 202
    assert state.started_request is not None
    assert state.started_request.source_paths == ("src",)
    assert state.started_request.operators == ("comparison",)


def test_ui_state_can_complete_run_synchronously() -> None:
    project_root = Path("tests/integration/fixtures/killed_project").resolve()

    def executor(options: RunOptions) -> ExecutionResult:
        config = load_config(options.project_root)
        session = SessionRunner(config).run()
        return ExecutionResult(
            session=session,
            report_path=project_root / ".mutation-tool" / "ui-test.json",
        )

    state = UIState(executor=executor)
    snapshot = state.run_blocking(RunRequest(project_root=str(project_root)))

    assert snapshot["status"] == "completed"
    assert snapshot["result"] is not None
