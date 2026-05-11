import importlib


# Helper to import the password module
def _password_module():
    return importlib.import_module("auth.password")


# Test that short passwords fail strength check
def test_short_password_is_rejected() -> None:
    assert _password_module().is_strong_password("Ab1!") is False


# Test that strong passwords pass all requirements
def test_strong_password_passes() -> None:
    assert _password_module().is_strong_password("StrongPass1!") is True


# Test that passwords without special chars fail
def test_missing_special_is_rejected() -> None:
    assert _password_module().is_strong_password("StrongPass1") is False


# Test that passwords without digits fail
def test_missing_digit_is_rejected() -> None:
    assert _password_module().is_strong_password("StrongPassword!") is False


# Test that passwords without uppercase fail
def test_missing_upper_is_rejected() -> None:
    assert _password_module().is_strong_password("strongpass1!") is False


# Test that short passwords are categorized as weak
def test_categorize_weak_for_short_password() -> None:
    assert _password_module().categorize_strength("abc") == "weak"


# Test that passwords meeting all criteria are strong
def test_categorize_strong_full_score() -> None:
    assert _password_module().categorize_strength("Abcdefghijk1!") == "strong"
