import seasons
import pytest


def test_seasons():

    assert seasons.number_to_words(seasons.date_converter("2023-12-23")) == "Five hundred twenty-seven thousand forty minutes"
    assert seasons.number_to_words(seasons.date_converter("2022-12-23")) == "One million, fifty-two thousand, six hundred forty minutes"

def test_error_seasons():

    with pytest.raises(ValueError):
        seasons.date_converter("January 1, 1999")

    with pytest.raises(ValueError):
        seasons.date_converter("2023-12")


