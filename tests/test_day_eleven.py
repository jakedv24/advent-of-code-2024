from solutions.day_eleven import blink_times, sanitize_leading_zeroes


def test_sanitize_zeroes():
    assert sanitize_leading_zeroes("00") == "0"
    assert sanitize_leading_zeroes("00100") == "100"


def test_multiple_blinks():
    stones = ["125", "17"]
    assert blink_times(6, stones) == 22
    assert blink_times(25, stones) == 55312