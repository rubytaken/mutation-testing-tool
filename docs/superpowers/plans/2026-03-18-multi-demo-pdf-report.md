# Multi-Demo UI and PDF Reporting Implementation Plan

> **For agentic workers:** REQUIRED: Use superpowers:subagent-driven-development (if subagents available) or superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add three selectable built-in demos, keep JSON report downloads, add PDF report downloads, and upgrade Turkish localization to real Unicode characters.

**Architecture:** The backend owns demo metadata and report generation. The UI fetches demo definitions, renders the selected demo experience, and downloads either JSON or PDF outputs from dedicated endpoints. Reports are produced from the same serialized session result so JSON and PDF stay consistent.

**Tech Stack:** Python 3.12, FastAPI, embedded HTML/JS UI, pytest, Ruff, MyPy

---

## File Structure

- Create: `src/mutation_tool/ui/demos.py`
- Create: `src/mutation_tool/reports/pdf_report.py`
- Create: `examples/ci_gate_demo/pyproject.toml`
- Create: `examples/ci_gate_demo/README.md`
- Create: `examples/ci_gate_demo/src/demo_app/__init__.py`
- Create: `examples/ci_gate_demo/src/demo_app/eligibility.py`
- Create: `examples/ci_gate_demo/tests/conftest.py`
- Create: `examples/ci_gate_demo/tests/test_eligibility.py`
- Create: `examples/timeout_lab_demo/pyproject.toml`
- Create: `examples/timeout_lab_demo/README.md`
- Create: `examples/timeout_lab_demo/src/demo_app/__init__.py`
- Create: `examples/timeout_lab_demo/src/demo_app/retry_logic.py`
- Create: `examples/timeout_lab_demo/tests/conftest.py`
- Create: `examples/timeout_lab_demo/tests/test_retry_logic.py`
- Modify: `src/mutation_tool/service.py`
- Modify: `src/mutation_tool/reports/__init__.py`
- Modify: `src/mutation_tool/reports/serialize.py`
- Modify: `src/mutation_tool/ui/app.py`
- Modify: `src/mutation_tool/ui/page.py`
- Modify: `tests/unit/test_ui.py`
- Modify: `tests/unit/test_service.py`
- Modify: `README.md`

### Task 1: Add Report Artifact Coverage First

**Files:**
- Modify: `tests/unit/test_service.py`
- Create: `tests/unit/test_reports.py`
- Modify: `src/mutation_tool/service.py`
- Create: `src/mutation_tool/reports/pdf_report.py`
- Modify: `src/mutation_tool/reports/__init__.py`

- [ ] **Step 1: Write the failing tests**

Add tests that expect:
- `execute_session(...)` to return both JSON and PDF paths
- the PDF writer to create a file that starts with `%PDF-`
- the PDF content bytes to contain visible section titles such as `Mutation Summary`

- [ ] **Step 2: Run tests to verify they fail**

Run: `python -m pytest tests/unit/test_service.py tests/unit/test_reports.py -q`
Expected: FAIL because PDF report support and extra paths do not exist yet.

- [ ] **Step 3: Write the minimal implementation**

Implement:
- `ReportArtifacts` style return data in `src/mutation_tool/service.py`
- a small text-based PDF writer in `src/mutation_tool/reports/pdf_report.py`
- exports in `src/mutation_tool/reports/__init__.py`

- [ ] **Step 4: Run tests to verify they pass**

Run: `python -m pytest tests/unit/test_service.py tests/unit/test_reports.py -q`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add tests/unit/test_service.py tests/unit/test_reports.py src/mutation_tool/service.py src/mutation_tool/reports/pdf_report.py src/mutation_tool/reports/__init__.py
git commit -m "feat: add pdf report generation"
```

### Task 2: Add Demo Catalog Coverage First

**Files:**
- Create: `src/mutation_tool/ui/demos.py`
- Modify: `tests/unit/test_ui.py`
- Modify: `src/mutation_tool/ui/app.py`

- [ ] **Step 1: Write the failing tests**

Add tests that expect:
- `/api/demos` to return three demos
- `/api/demo-preset?demo_id=beginner` to resolve the beginner project
- `/api/demo-preset?demo_id=ci_gate` and `timeout_lab` to resolve their own roots
- invalid ids to return `404`

- [ ] **Step 2: Run tests to verify they fail**

Run: `python -m pytest tests/unit/test_ui.py -q`
Expected: FAIL because the catalog endpoint and multi-demo lookup do not exist yet.

- [ ] **Step 3: Write the minimal implementation**

Implement:
- a typed demo catalog in `src/mutation_tool/ui/demos.py`
- `/api/demos`
- catalog-backed `/api/demo-preset`

- [ ] **Step 4: Run tests to verify they pass**

Run: `python -m pytest tests/unit/test_ui.py -q`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add src/mutation_tool/ui/demos.py src/mutation_tool/ui/app.py tests/unit/test_ui.py
git commit -m "feat: add demo catalog api"
```

### Task 3: Add the New Demo Fixtures

**Files:**
- Create: `examples/ci_gate_demo/...`
- Create: `examples/timeout_lab_demo/...`

- [ ] **Step 1: Write the failing fixture tests**

Add tests or targeted smoke coverage that assert:
- the new example tests pass under normal pytest
- the timeout demo includes a deterministic slow path

- [ ] **Step 2: Run tests to verify they fail**

Run: `python -m pytest examples/ci_gate_demo/tests examples/timeout_lab_demo/tests -q`
Expected: FAIL because the fixtures do not exist yet.

- [ ] **Step 3: Write the minimal implementation**

Create two small packages:
- `ci_gate_demo`: a survivor-friendly fixture with a strict preset
- `timeout_lab_demo`: a function with a predictable sleep path and tests that pass under normal conditions

- [ ] **Step 4: Run tests to verify they pass**

Run: `python -m pytest examples/ci_gate_demo/tests examples/timeout_lab_demo/tests -q`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add examples/ci_gate_demo examples/timeout_lab_demo
git commit -m "feat: add ci and timeout demo fixtures"
```

### Task 4: Update UI Rendering and Localization

**Files:**
- Modify: `src/mutation_tool/ui/page.py`
- Modify: `tests/unit/test_ui.py`

- [ ] **Step 1: Write the failing tests**

Extend UI tests to expect:
- demo selector copy
- JSON and PDF download buttons
- Unicode Turkish strings in the HTML payload

- [ ] **Step 2: Run tests to verify they fail**

Run: `python -m pytest tests/unit/test_ui.py -q`
Expected: FAIL because the new UI controls and copy are not present yet.

- [ ] **Step 3: Write the minimal implementation**

Update `page.py` to:
- render a demo selector
- show demo descriptions
- expose `Download Latest PDF`
- preserve English default
- use real Turkish characters in localized strings

- [ ] **Step 4: Run tests to verify they pass**

Run: `python -m pytest tests/unit/test_ui.py -q`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add src/mutation_tool/ui/page.py tests/unit/test_ui.py
git commit -m "feat: upgrade demo ui and unicode translations"
```

### Task 5: Wire Report Downloads End-to-End

**Files:**
- Modify: `src/mutation_tool/ui/app.py`
- Modify: `src/mutation_tool/service.py`
- Modify: `tests/unit/test_ui.py`

- [ ] **Step 1: Write the failing tests**

Add tests that expect:
- `/api/report/download?format=json` or equivalent JSON endpoint to still work
- a PDF download endpoint to return `application/pdf`

- [ ] **Step 2: Run tests to verify they fail**

Run: `python -m pytest tests/unit/test_ui.py -q`
Expected: FAIL because the PDF download endpoint does not exist yet.

- [ ] **Step 3: Write the minimal implementation**

Implement the latest-report download path for both formats while preserving backward compatibility for JSON downloads.

- [ ] **Step 4: Run tests to verify they pass**

Run: `python -m pytest tests/unit/test_ui.py -q`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add src/mutation_tool/ui/app.py src/mutation_tool/service.py tests/unit/test_ui.py
git commit -m "feat: add report download endpoints"
```

### Task 6: Update Documentation

**Files:**
- Modify: `README.md`
- Modify: `examples/beginner_demo/README.md`
- Create or modify: `examples/ci_gate_demo/README.md`
- Create or modify: `examples/timeout_lab_demo/README.md`

- [ ] **Step 1: Write the documentation changes**

Document:
- the three demos and what each teaches
- JSON vs PDF reports
- UI flow for selecting and running demos

- [ ] **Step 2: Verify examples match reality**

Run: `python -m mutation_tool ui`
Expected: the described UI controls and demo names match the docs.

- [ ] **Step 3: Commit**

```bash
git add README.md examples/beginner_demo/README.md examples/ci_gate_demo/README.md examples/timeout_lab_demo/README.md
git commit -m "docs: explain demos and report formats"
```

### Task 7: Final Verification

**Files:**
- Verify across the full repo

- [ ] **Step 1: Run the full test suite**

Run: `python -m pytest`
Expected: PASS

- [ ] **Step 2: Run lint**

Run: `python -m ruff check .`
Expected: PASS

- [ ] **Step 3: Run type checking**

Run: `python -m mypy src`
Expected: PASS

- [ ] **Step 4: Smoke-test the demo catalog**

Run: `python -m mutation_tool run examples/beginner_demo --max-mutants 10`
Expected: completes and writes JSON and PDF reports.

- [ ] **Step 5: Smoke-test the UI**

Run: `python -m mutation_tool ui`
Expected: English default, Turkish toggle, three demos, JSON/PDF download controls.
