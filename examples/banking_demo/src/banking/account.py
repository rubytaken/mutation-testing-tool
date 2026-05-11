"""Money operations — comparison and arithmetic mutations matter here."""
from __future__ import annotations


class InsufficientFundsError(Exception):
    """Raised when an account would go below zero."""


DEFAULT_DAILY_LIMIT = 1000.0


def withdraw(balance: float, amount: float, daily_limit: float = DEFAULT_DAILY_LIMIT) -> float:
    """Withdraw `amount` from `balance`, respecting daily limit and overdraft rules."""
    if amount <= 0:
        raise ValueError("amount must be positive")
    if amount > daily_limit:
        raise ValueError("amount exceeds daily limit")
    if amount > balance:
        raise InsufficientFundsError("not enough funds")
    return balance - amount


def transfer_fee(amount: float, is_premium: bool) -> float:
    """Tiered fee. Premium accounts pay nothing."""
    if is_premium:
        return 0.0
    if amount <= 100:
        return 1.0
    if amount <= 1000:
        return 2.5
    return round(amount * 0.005, 2)


def apply_daily_interest(balance: float, days: int, annual_rate: float = 0.03) -> float:
    """Compound daily interest over `days` days at the given annual rate."""
    if balance <= 0 or days <= 0:
        return balance
    daily_rate = annual_rate / 365
    return round(balance * (1 + daily_rate) ** days, 2)
