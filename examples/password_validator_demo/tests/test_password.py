import importlib


def _password_module():
    return importlib.import_module("auth.password")


def test_short_password_is_rejected() -> None:
    assert _password_module().is_strong_password("Ab1!") is False


def test_strong_password_passes() -> None:
    assert _password_module().is_strong_password("StrongPass1!") is True


def test_missing_special_is_rejected() -> None:
    assert _password_module().is_strong_password("StrongPass1") is False


def test_missing_digit_is_rejected() -> None:
    assert _password_module().is_strong_password("StrongPassword!") is False


def test_missing_upper_is_rejected() -> None:
    assert _password_module().is_strong_password("strongpass1!") is False


def test_categorize_weak_for_short_password() -> None:
    assert _password_module().categorize_strength("abc") == "weak"


def test_categorize_strong_full_score() -> None:
    assert _password_module().categorize_strength("Abcdefghijk1!") == "strong"
