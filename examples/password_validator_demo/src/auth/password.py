"""Password validation — comparison and boolean mutations live here."""
from __future__ import annotations

SPECIAL_CHARS = "!@#$%^&*"
MIN_LENGTH = 8
STRONG_LENGTH = 12


def is_strong_password(password: str) -> bool:
    """Return True only if password meets all rules.

    Rules: length >= 8, at least one uppercase letter, one digit,
    and one of the allowed special characters.
    """
    if len(password) < MIN_LENGTH:
        return False
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in SPECIAL_CHARS for c in password)
    return has_upper and has_digit and has_special


def categorize_strength(password: str) -> str:
    """Return one of 'weak', 'medium', 'strong' from a 0–5 point scale."""
    score = 0
    if len(password) >= MIN_LENGTH:
        score += 1
    if len(password) >= STRONG_LENGTH:
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in SPECIAL_CHARS for c in password):
        score += 1
    if score <= 2:
        return "weak"
    if score <= 4:
        return "medium"
    return "strong"
