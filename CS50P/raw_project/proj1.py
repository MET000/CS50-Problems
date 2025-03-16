import requests
import sys
import argparse
from tabulate import tabulate
from datetime import datetime
from colorama import Fore, Style

# Define the base URL for the API requests
url = "https://api.football-data.org/v4/competitions/"

# Headers needed for the API requests, including the authorization token
headers = {"X-Auth-Token": "f853bd1878124d0e8aee11db1a2e8446"}


def main():
    """
    Main function to handle command-line arguments and execute the respective functions
    to get the league table, top scorers, or upcoming matches.
    """

    # Create the argument parser with a description of the program
    parser = argparse.ArgumentParser(
        description=(
    "Get the table, top scorers, and upcoming matches for the league of your choice "
    "from the major European leagues and the Champions League. "
    "Available League IDs: "
    "Primera Division = PD, "
    "Serie A = SA, "
    "Premier League = PL, "
    "Bundesliga = BL1, "
    "Ligue 1 = FL1."
        )
    )

    # Add argument for league table with short flag -t
    parser.add_argument("-t", help="Provide table of the league of interest")

    # Add argument for upcoming matches with short flag -m
    parser.add_argument("-m", help="Provide upcoming matches of the league of interest")

    # Add argument for top scorers with short flag -s
    parser.add_argument("-s", help="Provide top scorers of the league of interest")

    # Parse the command-line arguments
    args = parser.parse_args()

    # Check if the table argument was provided
    if args.t:
        table = get_league_table(args.t)

        # Check if the result is not a list (indicating an error)
        if not isinstance(table, list):
            sys.exit(table)

        # Create a variable to define the alignment of columns for tabulate
        alignments = ["center"] * len(table[0])

        headers=[
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

        colored_headers = [Fore.YELLOW + Style.DIM + header + Style.RESET_ALL for header in headers]

        # Print the league table in a tabulated format
        print(
            tabulate(
                table,
                headers=colored_headers,
                tablefmt="rounded_outline",
                colalign=alignments,
            )
        )

    # Check if the scorers argument was provided
    elif args.s:
        scorers = get_league_scorers(args.s)

        # Check if the result is not a list (indicating an error)
        if not isinstance(scorers, list):
            sys.exit(scorers)

        # Create a variable to define the alignment of columns for tabulate
        alignments = ["center"] * len(scorers[0])

        headers=[
                    "Position",
                    "Player",
                    "Team",
                    "Played Matches",
                    "Goals",
                    "Assists",
                    "Penalties",
                ]

        colored_headers = [Fore.GREEN + Style.DIM + header + Style.RESET_ALL for header in headers]
        # Print the top scorers in a tabulated format
        print(
            tabulate(
                scorers,
                headers=colored_headers,
                tablefmt="rounded_outline",
                colalign=alignments,
            )
        )

    # Check if the matches argument was provided
    elif args.m:
        matches = get_league_matches(args.m)

        # Check if the result is not a list (indicating an error)
        if not isinstance(matches, list):
            sys.exit(matches)

        # Create a variable to define the alignment of columns for tabulate
        alignments = ["center"] * len(matches[0])

        # Print the upcoming matches in a tabulated format
        print(
            tabulate(
                matches,
                headers=["Match", "Date / Hour(UTC)", "Status"],
                tablefmt="rounded_outline",
                colalign=alignments,
            )
        )


def get_league_table(league_id):
    """
    Retrieve the standings table for the specified league.
    """
    global url
    global headers

    # Create the endpoint extension for the standings API request
    ext = f"{league_id}/standings"

    # Make the API request
    response = requests.get(url + ext, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the response JSON to get the table data
        table = response.json()["standings"][0]["table"]
        a = []

        # Iterate through the teams in the table
        for team in table:
            # Extract relevant data for each team
            position = team["position"]
            name = team["team"]["name"]
            played_games = team["playedGames"]
            points = team["points"]
            won = team["won"]
            drawn = team["draw"]
            lost = team["lost"]
            goals_for = team["goalsFor"]
            goals_against = team["goalsAgainst"]

            # Calculate the goal difference
            gd = int(goals_for) - int(goals_against)

            # Append the team's data to the list
            a.append(
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

            # Add an empty list to create more space between each row
            a.append([])

        # Return the standings table
        return a

    # Return an error message if the request failed
    return "An error occurred while fetching the data. Please check your request and try again."


def get_league_scorers(league_id):
    """
    Retrieve the top scorers for the specified league.
    """

    global url
    global headers

    # Create the endpoint extension for the scorers API request
    ext = f"{league_id}/scorers"

    # Make the API request
    response = requests.get(url + ext, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the response JSON to get the scorers data
        scorers = response.json()["scorers"]
        a = []
        # Create a variable that will be updated and used to determine the position of each team
        position = 0

        # Iterate through the scorers
        for scorer in scorers:
            # Extract relevant data for each scorer
            player_name = scorer["player"]["name"]
            team = scorer["team"]["name"]
            played_matches = scorer["playedMatches"]
            goals = scorer["goals"]
            assists = scorer["assists"] if scorer["assists"] is not None else "-"
            penalties = scorer["penalties"] if scorer["penalties"] is not None else "-"
            position += 1

            # Append the scorer's data to the list
            a.append(
                [position, player_name, team, played_matches, goals, assists, penalties]
            )

            # Add an empty list to create more space between each row
            a.append([])

        # Return the top scorers list
        return a

    # Return an error message if the request failed
    return "An error occurred while fetching the data. Please check your request and try again."


def get_league_matches(league_id):
    """
    Retrieve the scheduled matches for the specified league.
    """

    global url
    global headers

    # Create the endpoint extension for the matches API request
    ext = f"{league_id}/matches?status=SCHEDULED"

    # Make the API request
    response = requests.get(url + ext, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the response JSON to get the matches data
        matches = response.json()["matches"]
        a = []

        # Iterate through the matches
        for match in matches:
            # Skip matches with missing team names
            if match["homeTeam"]["name"] is None or match["awayTeam"]["name"] is None:
                continue
            else:
                # Extract relevant data for each match
                home_team = match["homeTeam"]["name"]
                away_team = match["awayTeam"]["name"]
                status = match["status"]
                date = datetime.strptime(match["utcDate"], "%Y-%m-%dT%H:%M:%SZ")
                if status == "SCHEDULED":

                    date = match["utcDate"].split("T")[0] + " (Not yet provided)"

                # Append the match's data to the list
                a.append([f"{home_team} vs {away_team}", date, status])

                # Add an empty list to create more space between each row
                a.append([])

        # Return the scheduled matches list
        return a

    # Return an error message if the request failed
    return "An error occurred while fetching the data. Please check your request and try again."


if __name__ == "__main__":
    main()
