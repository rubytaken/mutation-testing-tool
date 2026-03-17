def qualifies_for_priority(score: int) -> bool:
    return score >= 90


def shipping_message(score: int) -> str:
    return "priority" if qualifies_for_priority(score) else "standard"
