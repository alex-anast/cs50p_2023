from seasons import convert_to_seconds
import pytest


def test_convert_to_seconds_valid_date():
    assert convert_to_seconds("1999-01-01", "2000-01-01") == "Five hundred twenty-five thousand, six hundred minutes"
    assert convert_to_seconds("1999-12-31", "2000-01-01") == "One thousand, four hundred forty minutes"
    assert convert_to_seconds("1970-01-01", "2000-01-01") == "Fifteen million, seven hundred seventy-eight thousand eighty minutes"


def test_convert_to_seconds_invalid_date():
    with pytest.raises(SystemExit):
        convert_to_seconds("19991231")
    with pytest.raises(SystemExit):
        convert_to_seconds("1999-12") == "Invalid date"
    with pytest.raises(SystemExit):
        convert_to_seconds("1999") == "Invalid date"
    with pytest.raises(SystemExit):
        convert_to_seconds("1999-12-31-") == "Invalid date"
