from __future__ import annotations

from pathlib import Path

from mutation_tool.models import (
    BaselineResult,
    MutantResult,
    MutantStatus,
    MutationLocation,
    MutationSpec,
    SessionResult,
    ToolConfig,
)
from mutation_tool.reports import write_pdf_report


def test_write_pdf_report_creates_pdf_with_summary_sections(tmp_path: Path) -> None:
    output_path = tmp_path / "report.pdf"

    report_path = write_pdf_report(_build_sample_session(), output_path)

    content = report_path.read_bytes()
    assert report_path == output_path
    assert content.startswith(b"%PDF-")
    assert b"Mutation Summary" in content
    assert b"Recommended next steps" in content


def _build_sample_session() -> SessionResult:
    project_root = Path("demo-project").resolve()
    source_file = project_root / "src" / "demo_app" / "calculator.py"
    config = ToolConfig(
        project_root=project_root,
        source_paths=[project_root / "src"],
        test_command=["pytest", "-q"],
        exclude=["tests/**"],
        enabled_operators=["comparison"],
        timeout_multiplier=5.0,
        min_timeout=5.0,
        baseline_timeout=None,
        per_mutant_timeout=2.5,
        report_dir=project_root / ".mutation-tool",
    )
    baseline = BaselineResult(
        success=True,
        duration_seconds=0.42,
        exit_code=0,
        stdout="3 passed",
        stderr="",
        command=["pytest", "-q"],
    )
    mutant = MutantResult(
        spec=MutationSpec(
            mutant_id="comparison-1",
            file_path=source_file,
            operator_name="comparison",
            location=MutationLocation(8, 4, 8, 13),
            original_snippet="value > 0",
            mutated_snippet="value >= 0",
            description="Swap > with >=",
        ),
        status=MutantStatus.SURVIVED,
        duration_seconds=0.13,
        exit_code=0,
        stdout="3 passed",
        stderr="",
        timeout_seconds=2.5,
        failing_summary=None,
    )
    return SessionResult(
        config=config,
        baseline=baseline,
        mutants=[mutant],
        discovered_files=[source_file],
        generated_mutants=1,
    )
