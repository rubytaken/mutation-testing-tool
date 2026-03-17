from mutation_tool.engine.runner import extract_failure_summary, looks_like_error


def test_extract_failure_summary_prefers_failed_lines() -> None:
    output = "some line\nFAILED tests/test_app.py::test_value - assert 1 == 2\nother line\n"
    assert extract_failure_summary(output) == "FAILED tests/test_app.py::test_value - assert 1 == 2"


def test_looks_like_error_detects_collection_errors() -> None:
    assert looks_like_error(
        "ERROR collecting tests/test_app.py\nSyntaxError: invalid syntax"
    ) is True
    assert looks_like_error("FAILED tests/test_app.py::test_value - assert 1 == 2") is False
