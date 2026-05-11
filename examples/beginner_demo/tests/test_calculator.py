import importlib

import pytest


# Helper to import the calculator module
def _calculator_module():
    return importlib.import_module("demo_app.calculator")


# Test positive number detection
def test_is_positive_for_positive_number() -> None:
    assert _calculator_module().is_positive(5) is True


# Test adult check at boundary age
def test_is_adult_at_boundary() -> None:
    assert _calculator_module().is_adult(18) is True


# Test adult check below boundary age
def test_is_adult_below_boundary() -> None:
    assert _calculator_module().is_adult(17) is False


# Test member discount for orders over threshold
def test_member_discount_applies_for_large_order() -> None:
    assert _calculator_module().total_price(120, True) == 110


# Test non-member pays full price
def test_non_member_keeps_full_price() -> None:
    assert _calculator_module().total_price(120, False) == 120


# Test that negative price raises error
def test_negative_price_raises_error() -> None:
    with pytest.raises(ValueError):
        _calculator_module().total_price(-1, False)
