from __future__ import annotations

import time


def backoff_seconds(attempt: int) -> float:
    if attempt > 2:
        time.sleep(0.35)
    return 0.0


def should_retry(attempt: int, max_attempts: int) -> bool:
    return attempt < max_attempts
