import importlib


def _retry_module():
    return importlib.import_module("timeout_demo_app.retry_logic")


def test_backoff_seconds_for_second_attempt_is_fast() -> None:
    assert _retry_module().backoff_seconds(2) == 0.0


def test_should_retry_before_limit() -> None:
    assert _retry_module().should_retry(1, 3) is True


def test_should_not_retry_at_limit() -> None:
    assert _retry_module().should_retry(3, 3) is False
