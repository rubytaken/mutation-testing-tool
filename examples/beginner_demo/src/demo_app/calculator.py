def is_positive(value: int) -> bool:
    return value > 0


def is_adult(age: int) -> bool:
    return age >= 18


def total_price(price: int, is_member: bool) -> int:
    if price < 0:
        raise ValueError("price cannot be negative")
    if is_member and price >= 100:
        return price - 10
    return price
