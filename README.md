# Mutation Testing Tool

Beginner-friendly mutation testing tool for Python projects with a CLI, a local web UI, and JSON reports.

Documentation:

- English: `README.en.md`
- Turkce: `README.tr.md`
- Demo project: `examples/beginner_demo/README.md`

## Quick Start

```bash
python -m pip install -e .[dev]
python -m mutation_tool run . --max-mutants 10
python -m mutation_tool ui
```

Recommended project layout:

```text
project/
  pyproject.toml
  src/
  tests/
```

Recommended config:

```toml
[tool.mutation_tool]
source_paths = ["src"]
test_command = ["pytest", "-q"]
exclude = ["tests/**", "**/__pycache__/**"]
timeout_multiplier = 5.0
min_timeout = 5.0
```

Useful commands:

```bash
python -m mutation_tool list-operators
python -m mutation_tool run . --operator comparison --operator logical
python -m mutation_tool run . --stop-on-survivor
python -m mutation_tool run . --fail-on-survivor
python -m pytest
python -m mypy src
python -m ruff check .
```

What the tool does:

- creates small code mutations
- runs your test command after each mutation
- marks mutants as `killed`, `survived`, `timeout`, or `error`
- writes the latest report to `.mutation-tool/last-run.json`

Good first workflow:

1. Make sure the normal test suite is green.
2. Run a small mutation batch with `--max-mutants 10`.
3. Inspect survivors and add tests for the missing behavior.
4. Rerun until the weak spots shrink.
