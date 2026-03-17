from __future__ import annotations

import webbrowser
from pathlib import Path
from typing import Annotated

import typer
from rich.console import Console

from mutation_tool.operators import build_default_operators
from mutation_tool.reports import render_session
from mutation_tool.service import RunOptions, execute_options
from mutation_tool.ui import launch_ui

app = typer.Typer(add_completion=False, help="Introduce mutants and measure test effectiveness.")

PROJECT_ROOT_ARG = typer.Argument(exists=True, file_okay=False, dir_okay=True)
CONFIG_PATH_OPT = typer.Option("--config", exists=True, dir_okay=False)
SOURCE_OPT = typer.Option("--source", help="Override source path. Repeatable.")
OPERATOR_OPT = typer.Option("--operator", help="Enable specific operator. Repeatable.")
MAX_MUTANTS_OPT = typer.Option("--max-mutants", min=1)
TIMEOUT_OPT = typer.Option("--timeout", min=0.1)
FAIL_ON_SURVIVOR_OPT = typer.Option("--fail-on-survivor/--no-fail-on-survivor")


@app.command()
def run(
    project_root: Annotated[Path, PROJECT_ROOT_ARG] = Path("."),
    config_path: Annotated[Path | None, CONFIG_PATH_OPT] = None,
    source: Annotated[list[Path] | None, SOURCE_OPT] = None,
    operator: Annotated[list[str] | None, OPERATOR_OPT] = None,
    max_mutants: Annotated[int | None, MAX_MUTANTS_OPT] = None,
    per_mutant_timeout: Annotated[float | None, TIMEOUT_OPT] = None,
    fail_on_survivor: Annotated[bool | None, FAIL_ON_SURVIVOR_OPT] = None,
) -> None:
    console = Console()
    options = RunOptions(
        project_root=project_root,
        config_path=config_path,
        source_paths=tuple(source or []),
        operators=tuple(operator or []),
        max_mutants=max_mutants,
        per_mutant_timeout=per_mutant_timeout,
        fail_on_survivor=fail_on_survivor,
    )
    execution = execute_options(options)
    session = execution.session
    render_session(console, session, str(execution.report_path))

    if not session.baseline.success:
        raise typer.Exit(code=2)
    if session.config.fail_on_survivor and session.survived > 0:
        raise typer.Exit(code=1)


@app.command()
def ui(
    host: Annotated[str, typer.Option("--host")] = "127.0.0.1",
    port: Annotated[int, typer.Option("--port", min=1, max=65535)] = 8787,
    open_browser: Annotated[bool, typer.Option("--open-browser/--no-open-browser")] = True,
) -> None:
    url = f"http://{host}:{port}"
    if open_browser:
        webbrowser.open(url)
    launch_ui(host=host, port=port)


@app.command("list-operators")
def list_operators() -> None:
    console = Console()
    for operator in build_default_operators():
        console.print(operator.name)
