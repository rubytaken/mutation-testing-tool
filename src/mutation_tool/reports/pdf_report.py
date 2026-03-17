from __future__ import annotations

from pathlib import Path

from mutation_tool.models import MutantStatus, SessionResult
from mutation_tool.reports.serialize import build_guidance


def write_pdf_report(session: SessionResult, output_path: Path) -> Path:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    lines = _build_report_lines(session)
    content_stream = _build_content_stream(lines)
    pdf_bytes = _build_pdf_document(content_stream)
    output_path.write_bytes(pdf_bytes)
    return output_path


def _build_report_lines(session: SessionResult) -> list[str]:
    summary = session
    lines = [
        "Mutation Testing Tool Report",
        "",
        "Project",
        f"Project root: {session.config.project_root}",
        f"Source paths: {', '.join(str(path) for path in session.config.source_paths)}",
        "",
        "Baseline",
        f"Status: {'passed' if session.baseline.success else 'failed'}",
        f"Duration: {session.baseline.duration_seconds:.2f}s",
        f"Command: {' '.join(session.baseline.command)}",
        "",
        "Mutation Summary",
        f"Generated mutants: {summary.generated_mutants}",
        f"Executed mutants: {summary.executed}",
        f"Killed mutants: {summary.killed}",
        f"Survived mutants: {summary.survived}",
        f"Timed out mutants: {summary.timed_out}",
        f"Errored mutants: {summary.errors}",
        f"Mutation score: {summary.mutation_score:.1f}%",
        "",
        "Recommended next steps",
    ]

    guidance = build_guidance(session)
    if guidance:
        lines.extend(f"- {item}" for item in guidance)
    else:
        lines.append("- No extra guidance.")

    survivors = [result for result in session.mutants if result.status is MutantStatus.SURVIVED]
    if survivors:
        lines.extend(["", "Top surviving mutants"])
        for result in survivors[:10]:
            lines.append(
                "- "
                f"{result.spec.mutant_id} | "
                f"{result.spec.file_path}:{result.spec.location.start_line}"
            )
            lines.append(
                f"  {result.spec.original_snippet} -> {result.spec.mutated_snippet}"
            )

    return lines


def _build_content_stream(lines: list[str]) -> bytes:
    operations = ["BT", "/F1 12 Tf", "14 TL", "72 770 Td"]
    for index, line in enumerate(lines[:45]):
        if index > 0:
            operations.append("T*")
        operations.append(f"({_escape_pdf_text(line)}) Tj")
    operations.append("ET")
    return "\n".join(operations).encode("latin-1", "replace")


def _build_pdf_document(content_stream: bytes) -> bytes:
    objects = [
        b"<< /Type /Catalog /Pages 2 0 R >>",
        b"<< /Type /Pages /Kids [3 0 R] /Count 1 >>",
        (
            b"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] "
            b"/Contents 5 0 R /Resources << /Font << /F1 4 0 R >> >> >>"
        ),
        b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>",
        (
            f"<< /Length {len(content_stream)} >>\nstream\n".encode("ascii")
            + content_stream
            + b"\nendstream"
        ),
    ]

    parts: list[bytes] = [b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n"]
    offsets: list[int] = []
    for index, obj in enumerate(objects, start=1):
        offsets.append(sum(len(part) for part in parts))
        parts.append(f"{index} 0 obj\n".encode("ascii"))
        parts.append(obj)
        parts.append(b"\nendobj\n")

    xref_offset = sum(len(part) for part in parts)
    xref_parts: list[bytes] = [
        b"xref\n",
        f"0 {len(objects) + 1}\n".encode("ascii"),
        b"0000000000 65535 f \n",
    ]
    for offset in offsets:
        xref_parts.append(f"{offset:010d} 00000 n \n".encode("ascii"))

    trailer = (
        f"trailer\n<< /Size {len(objects) + 1} /Root 1 0 R >>\n"
        f"startxref\n{xref_offset}\n%%EOF\n"
    ).encode("ascii")
    return b"".join(parts + xref_parts + [trailer])


def _escape_pdf_text(value: str) -> str:
    return (
        value.replace("\\", "\\\\")
        .replace("(", "\\(")
        .replace(")", "\\)")
    )
