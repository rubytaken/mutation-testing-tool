from __future__ import annotations

import time


# Add delay after 2 attempts to simulate backoff strategy
def backoff_seconds(attempt: int) -> float:
    if attempt > 2:
        time.sleep(0.35)
    return 0.0


# Check if more retry attempts are allowed
def should_retry(attempt: int, max_attempts: int) -> bool:
    return attempt < max_attempts
