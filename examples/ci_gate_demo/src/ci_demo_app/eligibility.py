# Determine if score meets the priority threshold
def qualifies_for_priority(score: int) -> bool:
    return score >= 90


# Return shipping tier based on score qualification
def shipping_message(score: int) -> str:
    return "priority" if qualifies_for_priority(score) else "standard"
