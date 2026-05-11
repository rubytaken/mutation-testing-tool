import importlib

import pytest


def _account_module():
    return importlib.import_module("banking.account")


def test_normal_withdraw_subtracts_amount() -> None:
    assert _account_module().withdraw(500.0, 100.0) == 400.0


def test_withdraw_negative_amount_raises_value_error() -> None:
    with pytest.raises(ValueError):
        _account_module().withdraw(500.0, -10.0)


def test_withdraw_overdraft_raises_insufficient_funds() -> None:
    m = _account_module()
    with pytest.raises(m.InsufficientFundsError):
        m.withdraw(50.0, 100.0)


def test_premium_account_pays_no_fee() -> None:
    assert _account_module().transfer_fee(500.0, is_premium=True) == 0.0


def test_small_amount_pays_flat_fee() -> None:
    assert _account_module().transfer_fee(50.0, is_premium=False) == 1.0


def test_medium_amount_pays_higher_flat_fee() -> None:
    assert _account_module().transfer_fee(500.0, is_premium=False) == 2.5


def test_large_amount_pays_percentage_fee() -> None:
    # 5000 * 0.005 = 25.0
    assert _account_module().transfer_fee(5000.0, is_premium=False) == 25.0


def test_zero_days_interest_returns_balance_unchanged() -> None:
    assert _account_module().apply_daily_interest(1000.0, 0) == 1000.0


def test_one_year_interest_is_about_three_percent() -> None:
    result = _account_module().apply_daily_interest(1000.0, 365)
    assert 1029.0 < result < 1031.0
