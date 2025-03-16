from project import fetch_data, get_targeted_data, get_headers
import pytest


def test_fetch_data():
    """
    Test the fetch_data function for different league IDs and targets.
    Ensures the response contains the expected keys and structure.
    """
    data = fetch_data("PD", "scorers")
    assert "scorers" in data
    for i in data["scorers"]:
        assert "player" in i
    data = fetch_data("SA", "table")
    assert "standings" in data
    for i in data["standings"][0]["table"]:
        assert "position" in i
    data = fetch_data("BL1", "matches")
    assert "matches" in data
    for i in data["matches"]:
        assert "homeTeam" in i
    with pytest.raises(SystemExit):
        fetch_data("ZZ", "matches")


def test_get_targeted_data():
    """
    Test the get_targeted_data function for different responses.
    Ensures the extracted data has the expected length and structure.
    """
    response = fetch_data("FL1", "scorers")
    for i in get_targeted_data(response):
        assert len(i) == 5
    assert len(get_targeted_data(response)) == 10
    response = fetch_data("PD", "table")
    for i in get_targeted_data(response):
        assert len(i) == 10
    assert len(get_targeted_data(response)) == 20
    response = fetch_data("SA", "matches")
    for i in get_targeted_data(response):
        assert len(i) == 3
    assert len(get_targeted_data(response)) == 15


def test_get_headers():
    """
    Test the get_headers function for different targets.
    Ensures the returned headers match the expected lists.
    """
    assert get_headers("table") == [
        "Position",
        "Team",
        "Points",
        "Matches Played",
        "Won",
        "Drawn",
        "Lost",
        "Goals Scored",
        "Goals Conceded",
        "Goal Difference",
    ]

    assert get_headers("scorers") == [
        "Player",
        "Team",
        "Played Matches",
        "Goals",
        "Penalties",
    ]
    assert get_headers("matches") == ["Match", "Date / Hour(UTC)", "Status"]
