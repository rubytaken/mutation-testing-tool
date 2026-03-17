import importlib


def test_is_positive_for_positive_number() -> None:
    is_positive = importlib.import_module("sample_project.calculator").is_positive
    assert is_positive(2) is True


def test_is_positive_for_zero() -> None:
    is_positive = importlib.import_module("sample_project.calculator").is_positive
    assert is_positive(0) is False
