from __future__ import annotations

from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse, HTMLResponse
from pydantic import BaseModel, Field

from mutation_tool.ui.demos import get_demo, list_demos
from mutation_tool.ui.page import INDEX_HTML
from mutation_tool.ui.state import RunRequest, UIState


class RunPayload(BaseModel):
    project_root: str = "."
    config_path: str | None = None
    source_paths: list[str] = Field(default_factory=list)
    operators: list[str] = Field(default_factory=list)
    max_mutants: int | None = Field(default=None, ge=1)
    per_mutant_timeout: float | None = Field(default=None, gt=0)
    stop_on_survivor: bool | None = None
    fail_on_survivor: bool | None = None

    def to_request(self) -> RunRequest:
        return RunRequest(
            project_root=self.project_root,
            config_path=self.config_path,
            source_paths=tuple(self.source_paths),
            operators=tuple(self.operators),
            max_mutants=self.max_mutants,
            per_mutant_timeout=self.per_mutant_timeout,
            stop_on_survivor=self.stop_on_survivor,
            fail_on_survivor=self.fail_on_survivor,
        )


def create_app(state: UIState | None = None) -> FastAPI:
    app = FastAPI(title="Mutation Tool UI", version="0.1.0")
    ui_state = state or UIState()
    app.state.ui_state = ui_state

    @app.get("/", response_class=HTMLResponse)
    def index() -> str:
        return INDEX_HTML

    @app.get("/api/operators")
    def operators() -> dict[str, list[str]]:
        return {"operators": ui_state.available_operators()}

    @app.get("/api/status")
    def status() -> dict[str, object]:
        return ui_state.snapshot()

    @app.get("/api/demos")
    def demos() -> dict[str, object]:
        return {"demos": [demo.to_catalog_dict() for demo in list_demos()]}

    @app.get("/api/demo-preset")
    def demo_preset(demo_id: str = "beginner") -> dict[str, object]:
        demo = get_demo(demo_id)
        if demo is None:
            raise HTTPException(status_code=404, detail=f"Unknown demo id: {demo_id}")

        demo_root = Path(demo.request.project_root)
        if not demo_root.exists():
            raise HTTPException(status_code=404, detail="Built-in demo project was not found.")
        return demo.to_preset_dict()

    @app.post("/api/run", status_code=202)
    def run(payload: RunPayload) -> dict[str, object]:
        try:
            return ui_state.start_run(payload.to_request())
        except RuntimeError as exc:
            raise HTTPException(status_code=409, detail=str(exc)) from exc

    @app.get("/api/report/download")
    def download_report() -> FileResponse:
        report_path = _resolve_report_path(ui_state.snapshot(), "report_path")
        return FileResponse(
            path=report_path,
            media_type="application/json",
            filename=report_path.name,
        )

    @app.get("/api/report/download/pdf")
    def download_pdf_report() -> FileResponse:
        report_path = _resolve_report_path(
            ui_state.snapshot(),
            "pdf_report_path",
            missing_file_detail="The latest PDF report file was not found.",
        )
        return FileResponse(
            path=report_path,
            media_type="application/pdf",
            filename=report_path.name,
        )

    return app


def launch_ui(host: str = "127.0.0.1", port: int = 8787) -> None:
    import uvicorn

    uvicorn.run(create_app(), host=host, port=port)


def _resolve_report_path(
    snapshot: dict[str, object],
    field_name: str,
    *,
    missing_file_detail: str = "The latest report file was not found.",
) -> Path:
    report_path_value = snapshot.get(field_name)
    if not isinstance(report_path_value, str) or not report_path_value.strip():
        raise HTTPException(status_code=404, detail="No report is available yet.")

    report_path = Path(report_path_value)
    if not report_path.exists():
        raise HTTPException(status_code=404, detail=missing_file_detail)
    return report_path
