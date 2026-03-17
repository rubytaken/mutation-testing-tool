import importlib


def _eligibility_module():
    return importlib.import_module("ci_demo_app.eligibility")


def test_priority_for_high_score() -> None:
    assert _eligibility_module().qualifies_for_priority(95) is True


def test_standard_message_for_low_score() -> None:
    assert _eligibility_module().shipping_message(70) == "standard"
