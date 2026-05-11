import importlib


def _search_module():
    return importlib.import_module("algo.search")


def test_binary_search_finds_middle_element() -> None:
    assert _search_module().binary_search([1, 3, 5, 7, 9], 5) == 2


def test_binary_search_returns_minus_one_when_missing() -> None:
    assert _search_module().binary_search([1, 3, 5, 7], 4) == -1


def test_binary_search_finds_first_element() -> None:
    assert _search_module().binary_search([2, 4, 6], 2) == 0


def test_binary_search_finds_last_element() -> None:
    assert _search_module().binary_search([2, 4, 6], 6) == 2


def test_count_unique_value() -> None:
    assert _search_module().count_occurrences([1, 2, 3, 4], 3) == 1


def test_count_repeated_value() -> None:
    assert _search_module().count_occurrences([1, 2, 2, 2, 3], 2) == 3


def test_count_missing_value_is_zero() -> None:
    assert _search_module().count_occurrences([1, 2, 3], 99) == 0


def test_window_basic_sliding() -> None:
    assert _search_module().max_in_window([1, 3, 2, 5, 4], 3) == [3, 5, 5]


def test_window_larger_than_array_returns_global_max() -> None:
    assert _search_module().max_in_window([1, 2], 5) == [2]


def test_window_empty_array_returns_empty() -> None:
    assert _search_module().max_in_window([], 3) == []
