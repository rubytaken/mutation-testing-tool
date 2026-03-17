from __future__ import annotations

from rich.console import Console
from rich.table import Table

from mutation_tool.models import SessionResult
from mutation_tool.reports.serialize import build_guidance


def render_session(
    console: Console,
    session: SessionResult,
    json_report_path: str | None = None,
) -> None:
    console.print("[bold]Mutation Testing Tool[/bold]")
    console.print(f"Source files: {len(session.discovered_files)}")
    console.print(f"Generated mutants: {session.generated_mutants}")

    baseline_table = Table(title="Baseline")
    baseline_table.add_column("Status")
    baseline_table.add_column("Duration (s)")
    baseline_table.add_column("Command")
    baseline_table.add_row(
        "passed" if session.baseline.success else "failed",
        f"{session.baseline.duration_seconds:.2f}",
        " ".join(session.baseline.command),
    )
    console.print(baseline_table)

    summary_table = Table(title="Mutation Summary")
    summary_table.add_column("Score")
    summary_table.add_column("Killed")
    summary_table.add_column("Survived")
    summary_table.add_column("Timeout")
    summary_table.add_column("Error")
    summary_table.add_row(
        f"{session.mutation_score:.1f}%",
        str(session.killed),
        str(session.survived),
        str(session.timed_out),
        str(session.errors),
    )
    console.print(summary_table)

    guidance = build_guidance(session)
    if guidance:
        console.print("[bold]Guidance[/bold]")
        for item in guidance:
            console.print(f"- {item}")

    survivors = [result for result in session.mutants if result.status.value == "survived"]
    if survivors:
        detail_table = Table(title="Surviving Mutants")
        detail_table.add_column("Mutant")
        detail_table.add_column("Location")
        detail_table.add_column("Change")
        for result in survivors[:10]:
            detail_table.add_row(
                result.spec.mutant_id,
                f"{result.spec.file_path}:{result.spec.location.start_line}",
                f"{result.spec.original_snippet} -> {result.spec.mutated_snippet}",
            )
        console.print(detail_table)

    if json_report_path:
        console.print(f"JSON report: {json_report_path}")
