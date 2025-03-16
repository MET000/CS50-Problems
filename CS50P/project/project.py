import requests
import argparse
from tabulate import tabulate
from datetime import datetime
from colorama import Fore, Style
import sys

API_URL = "https://api.football-data.org/v4/competitions/"
API_KEY = {"X-Auth-Token": "f853bd1878124d0e8aee11db1a2e8446"}


def main():
    """
    Main function to execute the respective functions
    to get the league table, top scorers, or upcoming matches.
    """
    # Parse command-line arguments
    args, parser = parse_args()

    # Map arguments to their respective targets and colors
    args_data = {
        args.t: ["table", Fore.YELLOW],
        args.m: ["matches", Fore.GREEN],
        args.s: ["scorers", Fore.RED],
    }

    # Check which argument is provided and fetch the corresponding data
    if args.t or args.s or args.m:
        a = [[arg, args_data[arg][0], args_data[arg][1]] for arg in args_data if arg]
        league, target, color = a[0]
        response = fetch_data(league, target)
        targeted_data = get_targeted_data(response)
        headers = get_headers(target)
        display_table(targeted_data, headers, color)
    else:
        # Print help message if no arguments are provided
        sys.exit(parser.print_help())


def parse_args() -> list:
    """
    Parse command-line arguments for the script.

    Returns:
        list: A list containing the parsed arguments and the parser object.
    """
    # Create an argument parser
    parser = argparse.ArgumentParser(
        description=(
            "Get the table, top scorers, and upcoming matches for the league of your choice "
            "from the major European leagues and the Champions League. "
            "Available League IDs: "
            "Primera Division = PD, "
            "Serie A = SA, "
            "Premier League = PL, "
            "Bundesliga = BL1, "
            "Ligue 1 = FL1,"
            "Champions League = CL"
        )
    )

    # Add arguments for table, matches, and scorers
    parser.add_argument("-t", help="Provide table of the league of interest")
    parser.add_argument("-m", help="Provide upcoming matches of the league of interest")
    parser.add_argument("-s", help="Provide top scorers of the league of interest")
    args = parser.parse_args()

    return [args, parser]


def fetch_data(league_id: str, target: str) -> dict:
    """
    Fetch data from the API based on the league ID and target type.

    Args:
        league_id (str): The league ID.
        target (str): The type of data to fetch (table, scorers, matches).

    Returns:
        dict: The API response as a dictionary.
    """
    # Determine the endpoint based on the target type
    if target == "matches":
        ext = f"{league_id}/matches?status=SCHEDULED"
    elif target == "scorers":
        ext = f"{league_id}/scorers"
    elif target == "table":
        ext = f"{league_id}/standings"

    # Make the API request
    response = requests.get(API_URL + ext, headers=API_KEY)

    # Handle potential errors
    try:
        response.raise_for_status()
        return response.json()
    except requests.exceptions.ConnectionError:
        sys.exit(
            "Error: Unable to connect to the server. Please check your internet connection and try again."
        )
    except requests.exceptions.HTTPError as http_err:
        sys.exit(f"HTTP error occurred: {http_err}")
    except ValueError:
        sys.exit("Error: Received a bad response from the server.")
    except Exception as err:
        sys.exit(f"An unexpected error occurred: {err}")


def get_targeted_data(response: dict) -> list:
    """
    Extract targeted data from the API response.

    Args:
        response (dict): The API response.

    Returns:
        list: A list of extracted data based on the response type.
    """
    # Define extractors based on response type
    extractors = {
        "standings": lambda r: [
            [
                team["position"],
                team["team"]["name"],
                team["points"],
                team["playedGames"],
                team["won"],
                team["draw"],
                team["lost"],
                team["goalsFor"],
                team["goalsAgainst"],
                team["goalsFor"] - team["goalsAgainst"],
            ]
            for team in r["standings"][0]["table"]
        ],
        "scorers": lambda r: [
            [
                scorer["player"]["name"],
                scorer["team"]["name"],
                scorer["playedMatches"],
                scorer["goals"],
                scorer["penalties"] if scorer["penalties"] is not None else "-",
            ]
            for scorer in r["scorers"]
        ],
        "matches": lambda r: [
            [
                f"{match["homeTeam"]["name"]} vs {match["awayTeam"]["name"]}",
                (
                    str(datetime.strptime(match["utcDate"], "%Y-%m-%dT%H:%M:%SZ"))
                    if match["status"] == "TIMED"
                    else f"{match["utcDate"].split("T")[0]} (Not yet provided)"
                ),
                match["status"],
            ]
            for match in r["matches"][:15]
        ],
    }

    # Iterate through the extractors to get the targeted data
    for i in extractors:
        if i in response:
            return extractors[i](response)

    return []


def get_headers(target: str) -> list:
    """
    Get the headers for the table based on the target type.

    Args:
        target (str): The type of data (table, scorers, matches).

    Returns:
        list: A list of headers for the table.
    """
    # Define headers for league table
    if target == "table":
        headers = [
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

    # Define headers for top scorers
    elif target == "scorers":
        headers = ["Player", "Team", "Played Matches", "Goals", "Penalties"]

    # Define headers for upcoming matches
    elif target == "matches":
        headers = ["Match", "Date / Hour(UTC)", "Status"]

    return headers


def display_table(data: list, headers: list, color: str) -> None:
    """
    Display the data in a table format with colored headers.

    Args:
        data (list): The data to be displayed.
        headers (list): The headers for the table.
        color (str): The color for the headers.
    """

    # Prepare the table data
    table = data

    # Set the alignment for each column
    alignments = ["center"] * len(table[0])

    # Color the headers
    colored_headers = [color + header + Style.RESET_ALL for header in headers]

    # Print the table with the specified format and alignment
    print(
        tabulate(
            table,
            headers=colored_headers,
            tablefmt="rounded_grid",
            colalign=alignments,
        )
    )


if __name__ == "__main__":
    main()
