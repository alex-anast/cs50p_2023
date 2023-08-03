from working import convert
import pytest


def test_convert_valid():
    # Test valid inputs with different formats
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5:30 PM") == "09:00 to 17:30"


def test_convert_invalid():
    # Test invalid inputs with incorrect formats
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:00 PM")  # Invalid minutes (60)
    with pytest.raises(ValueError):
        convert("12:30 AM to 13:00 PM")  # Invalid hour (13)
    with pytest.raises(ValueError):
        convert("9 AM to 5 PM to 6 PM")  # Extra keyword "to"
    with pytest.raises(ValueError):
        convert("9:00 AM 5:00 PM")  # Missing "to" keyword
    with pytest.raises(ValueError):
        convert("9:00 AM to 5:00 PM to 6 PM")  # Extra "to" keyword
    with pytest.raises(ValueError):
        convert("9:00 AM to 5:00")  # Missing AM/PM


def test_convert_edge_cases():
    # Test edge cases with minimum and maximum hours
    assert convert("9:00 AM to 9:00 AM") == "09:00 to 09:00"
    assert convert("11:59 AM to 11:59 PM") == "11:59 to 23:59"
    assert convert("9:00 PM to 9:00 PM") == "21:00 to 21:00"
    assert convert("11:59 PM to 11:59 AM") == "23:59 to 11:59"
    assert convert("12:00 AM to 11:59 PM") == "00:00 to 23:59"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
