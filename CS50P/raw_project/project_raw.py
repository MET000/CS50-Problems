import requests
import argparse
from tabulate import tabulate
from datetime import datetime
from colorama import Fore, Style
import sys

API_URL = "https://api.football-data.org/v4/competitions/"
API_KEY = {"X-Auth-Token": "f853bd1878124d0e8aee11db1a2e8446"}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", help="Provide table of the league of interest")
    parser.add_argument("-m", help="Provide upcoming matches of the league of interest")
    parser.add_argument("-s", help="Provide top scorers of the league of interest")
    args = parser.parse_args()

    if args.t:
        response = fetch_data(args.t, "table")
        target = get_league_table(response)
        color = Fore.YELLOW

    elif args.s:
        response = fetch_data(args.s, "scorer")
        target = get_league_scorers(response)
        color = Fore.GREEN

    elif args.m:
        response = fetch_data(args.m, "matches")
        target = get_league_matches(response)
        color = Fore.BLUE

    display_table(target, color)


def get_league_table(data) -> list:

    table = data["standings"][0]["table"]
    league_data = [
        [
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
        ],
    ]
    for team in table:
        position = team["position"]
        name = team["team"]["name"]
        played_games = team["playedGames"]
        points = team["points"]
        won = team["won"]
        drawn = team["draw"]
        lost = team["lost"]
        goals_for = team["goalsFor"]
        goals_against = team["goalsAgainst"]
        gd = str(int(goals_for) - int(goals_against))
        league_data.append(
            [
                position,
                name,
                points,
                played_games,
                won,
                drawn,
                lost,
                goals_for,
                goals_against,
                gd,
            ]
        )
        league_data.append([])
    return league_data


def get_league_scorers(data) -> list:
    scorers = data["scorers"]
    scorers_data = [
        [
            "Position",
            "Player",
            "Team",
            "Played Matches",
            "Goals",
            "Assists",
            "Penalties",
        ],
    ]
    position = 0
    for scorer in scorers:
        player_name = scorer["player"]["name"]
        team = scorer["team"]["name"]
        played_matches = scorer["playedMatches"]
        goals = scorer["goals"]
        assists = scorer["assists"] if scorer["assists"] is not None else "-"
        penalties = scorer["penalties"] if scorer["penalties"] is not None else "-"
        position += 1
        scorers_data.append(
            [
                str(position),
                player_name,
                team,
                played_matches,
                goals,
                assists,
                penalties,
            ]
        )
        scorers_data.append([])
    return scorers_data


def get_league_matches(data) -> list:
    matches = data["matches"]
    matches_data = [
        ["Match", "Date / Hour(UTC)", "Status"],
    ]
    for match in matches:
        if len(matches_data) < 31:
            home_team = match["homeTeam"]["name"]
            away_team = match["awayTeam"]["name"]
            status = match["status"]
            date = datetime.strptime(match["utcDate"], "%Y-%m-%dT%H:%M:%SZ")
            if status == "SCHEDULED":
                date = match["utcDate"].split("T")[0] + " (Not yet provided)"
            matches_data.append([f"{home_team} vs {away_team}", str(date), status])
            matches_data.append([])
    return matches_data

def display_table(data: list, color) -> None:
    table = data
    alignments = ["center"] * len(table[0])
    colored_headers = [color + header + Style.RESET_ALL for header in table[0]]
    print(
        tabulate(
            table[1:],
            headers=colored_headers,
            tablefmt="rounded_outline",
            colalign=alignments,
        )
    )


def fetch_data(league_id, target):
    if target == "matches":
        ext = f"{league_id}/matches?status=SCHEDULED"
    elif target == "scorer":
        ext = f"{league_id}/scorers"
    elif target == "table":
        ext = f"{league_id}/standings"
    response = requests.get(API_URL + ext, headers=API_KEY)
    try:
        response.raise_for_status()
        print(response.json())
        return response.json()
    except requests.exceptions.ConnectionError:
        sys.exit("Error: Unable to connect to the server. Please check your internet connection and try again.")
    except requests.exceptions.HTTPError as http_err:
        sys.exit(f"HTTP error occurred: {http_err}")


if __name__ == "__main__":
    main()
