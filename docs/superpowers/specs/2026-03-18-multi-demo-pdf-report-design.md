# Multi-Demo UI and PDF Reporting Design

**Date:** 2026-03-18

**Status:** Approved for implementation

## Goal

Expand the existing UI from a single built-in demo into a small demo catalog, keep the machine-readable JSON report, add a human-readable PDF report, and make Turkish translations use real Unicode characters such as `ş`, `ğ`, `ü`, `ö`, `ç`, and `İ`.

## Problem Summary

The current UI teaches the tool through one built-in example and one JSON report file. That is enough for a first pass, but it leaves three user experience gaps:

1. Users cannot explore different mutation-testing learning scenarios without manually editing settings.
2. The JSON report is useful for tooling but is not ideal as a shareable report for humans.
3. Turkish localization currently avoids native characters, which makes the UI feel unfinished.

## Scope

### In Scope

- Add three selectable built-in demos:
  - `beginner`
  - `ci_gate`
  - `timeout_lab`
- Expose demo metadata through the UI backend
- Allow the UI to load or run the selected demo
- Keep JSON report download support
- Generate and download a PDF report for the latest run
- Upgrade Turkish translations to real Unicode characters
- Update tests and documentation

### Out of Scope

- Full HTML report pages
- User-authored custom demo definitions
- Theme-level localization beyond English and Turkish
- Rich charts in the PDF

## Recommended Approach

Use a backend-owned demo catalog plus backend-generated reports.

This keeps demo metadata, report generation, and file paths authoritative on the server. The UI stays lightweight and mostly renders what the backend describes. That is the cleanest extension of the current architecture and avoids coupling the browser to local filesystem assumptions.

## Architecture

### 1. Demo Catalog

Create a dedicated UI support module that defines three demo presets with:

- stable id
- localized display name
- localized summary
- localized learning goal
- resolved `project_root`
- `RunRequest` defaults

The backend will expose:

- `GET /api/demos`
- `GET /api/demo-preset?demo_id=<id>`

The old single-demo endpoint will be replaced by the catalog model to keep behavior explicit and extensible.

### 2. Report Outputs

The execution layer will keep writing `last-run.json` and will also produce `last-run.pdf` in the same report directory.

JSON remains the source of truth for structured data.

PDF becomes a presentation artifact generated from the same session result. The PDF should include:

- title and generated timestamp
- project root and source paths
- baseline status, duration, and command
- summary metrics
- guidance / next steps
- top surviving mutants
- timeout and error summaries when present

The PDF should be deterministic and dependency-light. The preferred implementation is a minimal text-oriented PDF writer generated in our codebase rather than introducing a heavy rendering dependency.

### 3. UI Integration

The UI will gain:

- a demo selector with three choices
- separate actions:
  - `Load Selected Demo`
  - `Run Selected Demo`
- clearer explanation text describing what each demo teaches
- download actions for:
  - latest JSON report
  - latest PDF report

The language switch remains in the top-right corner. English stays the default language.

### 4. Localization

The HTML and JavaScript payload should use real Unicode strings directly. Since the page content is embedded in Python, the page template must preserve JavaScript escapes safely while still allowing natural Unicode copy.

All new Turkish strings should use native characters consistently:

- `Türkçe`
- `İndir`
- `Özet`
- `Sonraki Adımlar`

## Proposed File Responsibilities

- `src/mutation_tool/ui/app.py`
  - add demo catalog and PDF download endpoints
- `src/mutation_tool/ui/page.py`
  - render demo selector, PDF download button, and localized copy
- `src/mutation_tool/ui/state.py`
  - continue serving latest run snapshot
- `src/mutation_tool/ui/demos.py`
  - new demo catalog definitions and lookup helpers
- `src/mutation_tool/reports/serialize.py`
  - expose data needed by both JSON and PDF reports
- `src/mutation_tool/reports/pdf_report.py`
  - new PDF report writer
- `src/mutation_tool/reports/__init__.py`
  - export the new writer
- `src/mutation_tool/service.py`
  - write both JSON and PDF artifacts and return their paths
- `tests/unit/test_ui.py`
  - demo catalog and download endpoint coverage
- `tests/unit/test_service.py`
  - report artifact generation coverage
- `tests/unit/test_reports.py`
  - new PDF writer coverage
- `examples/ci_gate_demo/...`
  - strict-quality demo fixture
- `examples/timeout_lab_demo/...`
  - timeout-oriented demo fixture
- `README.md`
  - explain demo catalog and both report formats

## Data Flow

1. UI loads `/api/demos` and renders selectable cards/options.
2. User selects a demo.
3. UI calls `/api/demo-preset?demo_id=...` to fill the form or runs that payload immediately.
4. `POST /api/run` starts the analysis as today.
5. Service executes the session and writes:
   - `last-run.json`
   - `last-run.pdf`
6. UI snapshot exposes both report paths.
7. User downloads either report through dedicated endpoints.

## Error Handling

- Unknown demo id returns `404`
- Missing latest JSON or PDF report returns `404`
- PDF generation failure should fail the run result only if it prevents report output integrity
- UI should show localized, human-readable errors for:
  - unknown demo
  - missing report
  - operator/status refresh failures

## Testing Strategy

### Backend

- demo catalog endpoint returns three demos
- demo preset endpoint resolves the correct project root per demo
- service writes both JSON and PDF reports
- PDF file begins with a valid PDF header and includes key sections

### UI

- English remains the static default
- Turkish can still be selected
- selector and both download buttons render
- demo metadata appears in the page payload

### Fixtures

- `beginner_demo`: survivor from weak boundary assertion
- `ci_gate_demo`: survivor plus `fail_on_survivor=True`
- `timeout_lab_demo`: deterministic slow path that can be used with a small timeout budget

## Risks and Mitigations

### Risk: PDF generation becomes dependency-heavy

Mitigation: keep the first version text-based and generate a simple PDF directly.

### Risk: Timeout demo becomes flaky across machines

Mitigation: design the fixture around a deterministic delay and pair it with an explicit small timeout in the preset.

### Risk: `page.py` grows further

Mitigation: if demo UI additions make the file harder to maintain, split backend demo metadata into `ui/demos.py` and keep page changes focused on rendering only.

## Success Criteria

- Users can choose among three demos in the UI
- JSON reports still download exactly as before
- PDF reports download successfully after a run
- English is the default UI language
- Turkish uses native characters correctly
- full test suite, Ruff, and MyPy pass
