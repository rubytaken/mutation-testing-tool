from pathlib import Path

from mutation_tool.engine.generator import apply_mutation_to_source, generate_mutations_for_file
from mutation_tool.operators import ComparisonOperator, NumericLiteralOperator


def test_generator_builds_comparison_mutation(tmp_path: Path) -> None:
    module = tmp_path / "module.py"
    module.write_text(
        "def is_positive(value):\n    return value > 0\n",
        encoding="utf-8",
    )

    mutations = generate_mutations_for_file(module, tmp_path, [ComparisonOperator()])

    assert len(mutations) == 1
    assert mutations[0].original_snippet == "value > 0"
    assert mutations[0].mutated_snippet == "value >= 0"


def test_generator_skips_no_mutate_lines(tmp_path: Path) -> None:
    module = tmp_path / "module.py"
    module.write_text(
        "VALUE = 1  # pragma: no mutate\n",
        encoding="utf-8",
    )

    mutations = generate_mutations_for_file(module, tmp_path, [NumericLiteralOperator()])

    assert mutations == []


def test_apply_mutation_replaces_exact_segment(tmp_path: Path) -> None:
    module = tmp_path / "module.py"
    source = "def f(x):\n    return x > 0\n"
    module.write_text(source, encoding="utf-8")

    mutation = generate_mutations_for_file(module, tmp_path, [ComparisonOperator()])[0]
    mutated = apply_mutation_to_source(source, mutation)

    assert "x >= 0" in mutated
