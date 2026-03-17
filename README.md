# Mutation Testing Tool

Beginner-friendly mutation testing tool for Python projects.

Documentation:

- English: `README.en.md`
- Turkce: `README.tr.md`
- Demo project: `examples/beginner_demo/README.md`

Quick commands:

```bash
python -m pip install -e .[dev]
python -m mutation_tool run .
python -m mutation_tool ui
python -m pytest
python -m mypy src
python -m ruff check .
```

What it does:

- makes small changes in your code
- runs your tests against each change
- shows whether tests catch the change
- reports weak spots in your test suite

Recommended starting point:

- use `pytest`
- put application code in `src/`
- put tests in `tests/`
- configure `[tool.mutation_tool]` in `pyproject.toml`
