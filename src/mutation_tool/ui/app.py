from __future__ import annotations

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field

from mutation_tool.ui.page import INDEX_HTML
from mutation_tool.ui.state import RunRequest, UIState


class RunPayload(BaseModel):
    project_root: str = "."
    config_path: str | None = None
    source_paths: list[str] = Field(default_factory=list)
    operators: list[str] = Field(default_factory=list)
    max_mutants: int | None = Field(default=None, ge=1)
    per_mutant_timeout: float | None = Field(default=None, gt=0)
    fail_on_survivor: bool | None = None

    def to_request(self) -> RunRequest:
        return RunRequest(
            project_root=self.project_root,
            config_path=self.config_path,
            source_paths=tuple(self.source_paths),
            operators=tuple(self.operators),
            max_mutants=self.max_mutants,
            per_mutant_timeout=self.per_mutant_timeout,
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

    @app.post("/api/run", status_code=202)
    def run(payload: RunPayload) -> dict[str, object]:
        try:
            return ui_state.start_run(payload.to_request())
        except RuntimeError as exc:
            raise HTTPException(status_code=409, detail=str(exc)) from exc

    return app


def launch_ui(host: str = "127.0.0.1", port: int = 8787) -> None:
    import uvicorn

    uvicorn.run(create_app(), host=host, port=port)
