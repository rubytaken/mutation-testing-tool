"""Search and windowing — a playground for off-by-one mutations."""
from __future__ import annotations


def binary_search(arr: list[int], target: int) -> int:
    """Iterative binary search on a sorted list. Returns index, or -1."""
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def count_occurrences(arr: list[int], target: int) -> int:
    """Count how many times target appears in a sorted list."""
    if not arr:
        return 0

    # find leftmost
    low, high = 0, len(arr) - 1
    first = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            first = mid
            high = mid - 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    if first == -1:
        return 0

    # find rightmost
    low, high = 0, len(arr) - 1
    last = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            last = mid
            low = mid + 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return last - first + 1


def max_in_window(arr: list[int], window: int) -> list[int]:
    """Sliding window maximum (naive implementation)."""
    if not arr or window <= 0:
        return []
    if window > len(arr):
        return [max(arr)]
    return [max(arr[i:i + window]) for i in range(len(arr) - window + 1)]
