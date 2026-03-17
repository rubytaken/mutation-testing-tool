from __future__ import annotations

from pathlib import Path

from mutation_tool.models import SessionResult


def session_to_dict(
    session: SessionResult,
    report_path: Path | None = None,
) -> dict[str, object]:
    payload: dict[str, object] = {
        "config": {
            "project_root": str(session.config.project_root),
            "source_paths": [str(path) for path in session.config.source_paths],
            "test_command": session.config.test_command,
            "exclude": session.config.exclude,
            "enabled_operators": session.config.enabled_operators,
            "timeout_multiplier": session.config.timeout_multiplier,
            "min_timeout": session.config.min_timeout,
            "baseline_timeout": session.config.baseline_timeout,
            "per_mutant_timeout": session.config.per_mutant_timeout,
            "report_dir": str(session.config.report_dir),
            "max_mutants": session.config.max_mutants,
            "stop_on_survivor": session.config.stop_on_survivor,
            "fail_on_survivor": session.config.fail_on_survivor,
        },
        "baseline": {
            "success": session.baseline.success,
            "duration_seconds": session.baseline.duration_seconds,
            "exit_code": session.baseline.exit_code,
            "command": session.baseline.command,
            "stdout": session.baseline.stdout,
            "stderr": session.baseline.stderr,
        },
        "summary": {
            "discovered_files": [str(path) for path in session.discovered_files],
            "generated_mutants": session.generated_mutants,
            "executed": session.executed,
            "killed": session.killed,
            "survived": session.survived,
            "timeout": session.timed_out,
            "error": session.errors,
            "mutation_score": session.mutation_score,
        },
        "guidance": build_guidance(session),
        "mutants": [
            {
                "mutant_id": result.spec.mutant_id,
                "file_path": str(result.spec.file_path),
                "operator_name": result.spec.operator_name,
                "description": result.spec.description,
                "location": {
                    "start_line": result.spec.location.start_line,
                    "start_col": result.spec.location.start_col,
                    "end_line": result.spec.location.end_line,
                    "end_col": result.spec.location.end_col,
                },
                "original_snippet": result.spec.original_snippet,
                "mutated_snippet": result.spec.mutated_snippet,
                "status": result.status.value,
                "duration_seconds": result.duration_seconds,
                "exit_code": result.exit_code,
                "timeout_seconds": result.timeout_seconds,
                "failing_summary": result.failing_summary,
                "stdout": result.stdout,
                "stderr": result.stderr,
            }
            for result in session.mutants
        ],
    }
    if report_path is not None:
        payload["report_path"] = str(report_path)
    return payload


def build_guidance(session: SessionResult) -> list[str]:
    guidance: list[str] = []

    if not session.baseline.success:
        guidance.append(
            "Baseline test run failed. Fix the normal test suite first, "
            "then rerun mutation analysis."
        )
        return guidance

    if session.executed == 0:
        guidance.append(
            "No mutants were executed. Check the source paths, exclude rules, "
            "and enabled operators."
        )
        return guidance

    if session.survived > 0:
        guidance.append(
            f"{session.survived} mutant(s) survived. Add focused assertions "
            "around the changed behavior."
        )
    if session.timed_out > 0:
        guidance.append(
            f"{session.timed_out} mutant(s) timed out. Review loops, waits, "
            "or raise the timeout budget."
        )
    if session.errors > 0:
        guidance.append(
            f"{session.errors} mutant(s) produced import or syntax issues. "
            "Inspect the generated change details."
        )
    if session.executed > 0 and not any((session.survived, session.timed_out, session.errors)):
        guidance.append(
            "All executed mutants were detected. Increase the scope or mutant "
            "count to probe more behavior."
        )

    return guidance
