from working import convert
import pytest


def test_convert1():

    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 PM to 5 AM") == "21:00 to 05:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"

def test_convert_error():

    with pytest.raises(ValueError):
        convert("cat")

    with pytest.raises(ValueError):
        convert("00:00 to 10:00 PM")

    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")

    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")






