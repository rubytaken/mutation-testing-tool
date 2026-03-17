import importlib


def test_identity_returns_value() -> None:
    identity = importlib.import_module("sample_project.math_utils").identity
    assert identity(7) == 7
