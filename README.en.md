# Mutation Testing Tool - English Guide

This guide explains what the program does, why you would use it, how to configure it, how to run it from the CLI or the UI, and what kind of tests you should write if you are a beginner.

Ready-made practice project:

- `examples/beginner_demo/README.md`

## 1. What is this program?

`mutation-tool` is a Python mutation testing tool.

Normal testing answers this question:

- "Does my code pass the tests I wrote?"

Mutation testing answers a stronger question:

- "Are my tests strong enough to notice small bugs in my code?"

The tool makes tiny changes in your source code, one change at a time, and runs your test suite after each change.

Example:

- your code has `value > 0`
- the tool changes it to `value >= 0`
- if tests fail, the mutant is `killed`
- if tests still pass, the mutant `survived`

If a mutant survives, it usually means your tests are missing an important case.

## 2. Why is this useful?

Code coverage tells you that a line was executed.

Mutation testing tells you whether your test really checked the behavior of that line.

That means this tool helps you:

- find weak tests
- find missing edge cases
- improve confidence in your code
- build better regression tests

## 3. What does the tool do internally?

When you run it, the tool follows this flow:

1. Reads configuration from `pyproject.toml`
2. Finds Python files inside the configured `source_paths`
3. Runs a baseline test command first
4. Stops immediately if baseline tests already fail
5. Parses source files with Python `ast`
6. Generates small mutations such as:
   - `>` -> `>=`
   - `True` -> `False`
   - `and` -> `or`
   - `+` -> `-`
7. Copies your project into a temporary workspace
8. Applies one mutant in that temporary copy
9. Runs your test command on that mutated copy
10. Saves the result
11. Writes a JSON report to `.mutation-tool/last-run.json`

Important:

- it does not mutate your real source files directly during a normal run
- it works on temporary copies

## 4. Result meanings

- `killed`: your tests failed, so they caught the mutant
- `survived`: your tests passed, so they did not notice the bug
- `timeout`: the mutant run took too long
- `error`: the mutant caused an invalid test run or broken import/syntax

## 5. Recommended project structure

For beginners, use this layout:

```text
your-project/
  pyproject.toml
  src/
    your_package/
      __init__.py
      calculator.py
  tests/
    test_calculator.py
```

Recommended test framework:

- best choice: `pytest`

Why `pytest`?

- easiest for beginners
- short syntax
- very common in Python projects
- already the default in this tool

## 6. Installation

### Step 1: Create and activate a virtual environment

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

Linux/macOS:

```bash
python -m venv .venv
source .venv/bin/activate
```

### Step 2: Install the tool and development dependencies

```bash
python -m pip install -e .[dev]
```

## 7. Basic configuration

Add this to your project's `pyproject.toml`:

```toml
[tool.mutation_tool]
source_paths = ["src"]
test_command = ["pytest", "-q"]
exclude = ["tests/**", "**/__pycache__/**"]
timeout_multiplier = 5.0
min_timeout = 5.0
```

Meaning of each field:

- `source_paths`: folders or files that should be mutated
- `test_command`: command used to run tests
- `exclude`: files/folders that should not be mutated
- `timeout_multiplier`: per-mutant timeout based on baseline runtime
- `min_timeout`: minimum timeout in seconds

## 8. What should I put in `source_paths`?

Usually:

- use `src` if your real application code is in `src/`
- use a package path like `app` if your project uses `app/`
- do not point this to `tests/`

Good examples:

```toml
source_paths = ["src"]
```

```toml
source_paths = ["src/my_package"]
```

```toml
source_paths = ["src/my_package/service.py"]
```

## 9. What can I use for tests?

### Recommended: `pytest`

Use this if you are new:

```toml
test_command = ["pytest", "-q"]
```

You can also run a subset:

```toml
test_command = ["pytest", "-q", "tests"]
```

### Also possible: `unittest`

This tool is CLI-driven, so any command that:

- runs tests
- returns `0` when tests pass
- returns non-zero when tests fail

can be used.

Example with `unittest`:

```toml
test_command = ["python", "-m", "unittest", "discover", "-s", "tests", "-v"]
```

Still, for beginners I strongly recommend `pytest`.

## 10. First example from scratch

### Application code

File: `src/sample_project/calculator.py`

```python
def is_positive(value: int) -> bool:
    return value > 0
```

### Test code

File: `tests/test_calculator.py`

```python
from sample_project.calculator import is_positive


def test_positive_number() -> None:
    assert is_positive(5) is True


def test_zero_is_not_positive() -> None:
    assert is_positive(0) is False
```

Why is this good?

- first test checks the normal case
- second test checks the boundary case
- if the code changes from `>` to `>=`, the second test should fail

That means the mutant will be killed.

## 11. How to run it from the command line

### Basic run

```bash
python -m mutation_tool run .
```

### Limit the number of mutants

```bash
python -m mutation_tool run . --max-mutants 10
```

### Run only specific operator types

```bash
python -m mutation_tool run . --operator comparison --operator logical
```

### Show available operators

```bash
python -m mutation_tool list-operators
```

## 12. How to use the local UI

Start the UI:

```bash
python -m mutation_tool ui
```

Then open:

```text
http://127.0.0.1:8787
```

### UI fields explained

#### `Project root`

What to enter:

- the main folder of the project you want to test

Examples:

- `.`
- `C:\Users\YourName\Desktop\my-project`

Use `.` if you already opened the terminal inside the project.

#### `Config path`

What to enter:

- optional path to a specific config file

Usually leave this empty.

Use it only if:

- your config is not in the default `pyproject.toml`
- or you want to point to a different config file manually

#### `Source paths`

What to enter:

- the code location you want to mutate
- write multiple entries separated by commas

Examples:

- `src`
- `src/my_package`
- `src/my_package/service.py`
- `src,src/my_package/utils.py`

For beginners, write:

- `src`

#### `Operators`

What to do:

- choose mutation types from the list
- or leave it unselected to use all default operators

If you are new, leave it empty first.

#### `Max mutants`

What to enter:

- a small number like `5`, `10`, or `20` when learning

Why?

- faster runs
- easier to inspect results

For first use, I recommend:

- `10`

#### `Timeout (sec)`

What to enter:

- maximum seconds per mutant run

If you are unsure:

- leave it empty

The tool can calculate a timeout from the baseline test runtime.

#### `Fail run when a survivor appears`

What it means:

- if enabled, the run is treated as failed when at least one mutant survives

Useful for:

- CI pipelines
- strict quality gates

For first learning runs:

- usually leave it unchecked

## 13. Beginner workflow: start to finish

If you know nothing yet, do this exact order:

1. Create a small Python project
2. Put code under `src/`
3. Put tests under `tests/`
4. Install `pytest`
5. Make sure normal tests pass first:

```bash
python -m pytest
```

6. Add mutation config to `pyproject.toml`
7. Run a small mutation session first:

```bash
python -m mutation_tool run . --max-mutants 10
```

8. Or use the UI:

```bash
python -m mutation_tool ui
```

9. Look at survivors
10. Add tests for the missing behavior
11. Run mutation testing again

## 14. What tests should I write?

This is the most important part.

Weak test:

- only checks one normal input

Stronger test:

- checks normal case
- checks edge case
- checks invalid input if relevant
- checks both true and false paths
- checks returned value exactly

You should test:

- boundary values like `0`, `1`, `-1`
- empty values like `""`, `[]`, `{}` if relevant
- `None` if your function accepts it
- exception behavior
- boolean decisions
- branches in `if/else`
- loops and stop conditions
- side effects such as file writes or database updates

### Very useful `pytest` patterns

#### Exact assertions

```python
def test_total() -> None:
    assert calculate_total(10, 2) == 12
```

#### Boundary test

```python
def test_zero_case() -> None:
    assert is_positive(0) is False
```

#### Exception test

```python
import pytest


def test_negative_age_raises() -> None:
    with pytest.raises(ValueError):
        validate_age(-1)
```

#### Parameterized test

```python
import pytest


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        (5, True),
        (0, False),
        (-3, False),
    ],
)
def test_is_positive(value: int, expected: bool) -> None:
    assert is_positive(value) is expected
```

## 15. What should I do when a mutant survives?

Suppose the tool says this survived:

- original: `value > 0`
- mutated: `value >= 0`

That tells you:

- your tests do not distinguish between `0` and positive numbers

So add a test like:

```python
def test_zero_is_not_positive() -> None:
    assert is_positive(0) is False
```

That is the core mutation testing workflow:

- see survivor
- understand what behavior changed
- add a test for that behavior
- rerun

## 16. Recommended first strategy

If your project is large, do not run everything immediately.

Start with:

- one small module
- `--max-mutants 10`
- default operators

Then grow slowly.

Good first command:

```bash
python -m mutation_tool run . --max-mutants 10
```

## 17. Common mistakes

### Baseline tests already fail

Problem:

- mutation run stops immediately

What to do:

- fix normal tests first
- mutation testing only makes sense on a green test suite

### Mutating the wrong folder

Problem:

- you set `source_paths` to `tests`

What to do:

- point it to application code, usually `src`

### Only happy-path tests

Problem:

- many mutants survive

What to do:

- add edge-case tests
- add false-path tests
- add exact assertions

### Running too many mutants at the beginning

Problem:

- it feels slow and overwhelming

What to do:

- use `--max-mutants 5` or `10` first

## 18. Where do I find the results?

- terminal summary in the CLI
- browser dashboard in the UI
- JSON file in `.mutation-tool/last-run.json`

## 19. How do I test this tool itself?

If you are developing this mutation-testing project itself, use:

```bash
python -m pytest
python -m mypy src
python -m ruff check .
```

This project currently uses:

- `pytest` for tests
- `mypy` for static typing
- `ruff` for linting
- `FastAPI TestClient` for UI/API endpoint tests

## 20. Best beginner setup

If you want the simplest path, use this:

- tests: `pytest`
- source folder: `src`
- config:

```toml
[tool.mutation_tool]
source_paths = ["src"]
test_command = ["pytest", "-q"]
exclude = ["tests/**", "**/__pycache__/**"]
timeout_multiplier = 5.0
min_timeout = 5.0
```

- first run:

```bash
python -m mutation_tool run . --max-mutants 10
```

- first UI run:

```bash
python -m mutation_tool ui
```

If you do only that, you already have a solid beginner workflow.
