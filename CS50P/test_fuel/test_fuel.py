from fuel import convert, gauge
import pytest


def test_convert():

    assert convert("4/4") == 100
    assert convert("3/4") == 75
    assert convert("1/4") == 25


def test_convert_errors():

    with pytest.raises(ValueError):

        convert("4/3")

    with pytest.raises(ZeroDivisionError):

        convert("4/0")


def test_gauge():

    assert gauge(1) == 'E'
    assert gauge(99) == 'F'
    assert gauge(75) == '75%'
