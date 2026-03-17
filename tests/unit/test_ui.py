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
    assert "How To Use Mutation Lab" in response.text
    assert "Choose a demo" in response.text
    assert "Load Selected Demo" in response.text
    assert "Run Selected Demo" in response.text
    assert "Download Latest Report" in response.text
    assert "Download Latest PDF" in response.text
    assert "Başlangıç Demosu" in response.text
    assert 'id="lang-en-button"' in response.text
    assert 'id="lang-tr-button"' in response.text


def test_ui_exposes_operator_list() -> None:
    client = TestClient(create_app(StubState()))

    response = client.get("/api/operators")

    assert response.status_code == 200
    assert response.json() == {"operators": ["comparison", "logical"]}


def test_ui_exposes_demo_catalog() -> None:
    client = TestClient(create_app(StubState()))

    response = client.get("/api/demos")

    assert response.status_code == 200
    payload = response.json()
    assert [demo["id"] for demo in payload["demos"]] == ["beginner", "ci_gate", "timeout_lab"]


def test_ui_exposes_demo_preset() -> None:
    client = TestClient(create_app(StubState()))

    response = client.get("/api/demo-preset", params={"demo_id": "beginner"})

    assert response.status_code == 200
    payload = response.json()
    assert payload["request"]["source_paths"] == ["src"]
    assert Path(payload["request"]["project_root"]).name == "beginner_demo"


def test_ui_exposes_ci_gate_demo_preset() -> None:
    client = TestClient(create_app(StubState()))

    response = client.get("/api/demo-preset", params={"demo_id": "ci_gate"})

    assert response.status_code == 200
    payload = response.json()
    assert Path(payload["request"]["project_root"]).name == "ci_gate_demo"
    assert payload["request"]["fail_on_survivor"] is True


def test_ui_exposes_timeout_demo_preset() -> None:
    client = TestClient(create_app(StubState()))

    response = client.get("/api/demo-preset", params={"demo_id": "timeout_lab"})

    assert response.status_code == 200
    payload = response.json()
    assert Path(payload["request"]["project_root"]).name == "timeout_lab_demo"
    assert payload["request"]["per_mutant_timeout"] == 0.2


def test_ui_rejects_unknown_demo_id() -> None:
    client = TestClient(create_app(StubState()))

    response = client.get("/api/demo-preset", params={"demo_id": "nope"})

    assert response.status_code == 404


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
            "stop_on_survivor": True,
        },
    )

    assert response.status_code == 202
    assert state.started_request is not None
    assert state.started_request.source_paths == ("src",)
    assert state.started_request.operators == ("comparison",)
    assert state.started_request.stop_on_survivor is True


def test_ui_state_can_complete_run_synchronously() -> None:
    project_root = Path("tests/integration/fixtures/killed_project").resolve()

    def executor(options: RunOptions) -> ExecutionResult:
        config = load_config(options.project_root)
        session = SessionRunner(config).run()
        return ExecutionResult(
            session=session,
            report_path=project_root / ".mutation-tool" / "ui-test.json",
            pdf_report_path=project_root / ".mutation-tool" / "ui-test.pdf",
        )

    state = UIState(executor=executor)
    snapshot = state.run_blocking(RunRequest(project_root=str(project_root)))

    assert snapshot["status"] == "completed"
    assert snapshot["result"] is not None


def test_ui_report_download_endpoint_returns_latest_report(tmp_path: Path) -> None:
    report_path = tmp_path / "last-run.json"
    report_path.write_text('{"ok": true}', encoding="utf-8")

    class ReportState(StubState):
        def snapshot(self) -> dict[str, object]:
            return {
                "status": "completed",
                "message": "Done",
                "report_path": str(report_path),
                "result": {},
            }

    client = TestClient(create_app(ReportState()))

    response = client.get("/api/report/download")

    assert response.status_code == 200
    assert response.headers["content-type"].startswith("application/json")
    assert response.text == '{"ok": true}'


def test_ui_pdf_report_download_endpoint_returns_latest_pdf(tmp_path: Path) -> None:
    report_path = tmp_path / "last-run.pdf"
    report_path.write_bytes(b"%PDF-1.4\nmock")

    class ReportState(StubState):
        def snapshot(self) -> dict[str, object]:
            return {
                "status": "completed",
                "message": "Done",
                "report_path": str(tmp_path / "last-run.json"),
                "pdf_report_path": str(report_path),
                "result": {},
            }

    client = TestClient(create_app(ReportState()))

    response = client.get("/api/report/download/pdf")

    assert response.status_code == 200
    assert response.headers["content-type"].startswith("application/pdf")
    assert response.content.startswith(b"%PDF-1.4")
