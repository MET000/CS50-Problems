# Soccer Stats CLI: Real-Time Data for Major Leagues
#### Video Demo: https://youtu.be/bl5Ptyq6Hws
#### Description:

The **Soccer Stats CLI: Real-Time Data for Major Leagues** project is a command-line application designed to provide football enthusiasts with up-to-date information about major European football leagues and the Champions League. The application fetches real-time data from the Football Data API and presents it in a clear and user-friendly tabulated format. This tool is invaluable for fans who want to stay informed about their favorite leagues, teams, and players.

### Key Features:

- **League Table**: Displays the current standings of teams in the specified league, including their position, team name, points, matches played, wins, draws, losses, goals scored, goals conceded, and goal difference.
- **Top Scorers**: Lists the top scorers in the specified league, including their position, player name, team, matches played, goals, and penalties.
- **Upcoming Matches**: Provides a list of the next 15 upcoming matches in the specified league, including the teams playing, the date and time of the match, and the match status.

### Design Choices:
- **Command-Line Interface**: The decision to use a command-line interface (CLI) was made to keep the application lightweight and easy to use without requiring a graphical user interface (GUI).
- **Tabulate Library**: The `tabulate` library was chosen for formatting the output data into easy-to-read tables. It provides various table formats and alignment options that enhance the readability of the output.
- **Colorama Library**: The `colorama` library was used to add color to the table headers, making them visually distinct and improving the user experience.
- **Data Fetching**: The application uses the Football Data API to fetch real-time data, ensuring that the information provided is up-to-date and accurate.

### How to Use:
1. **Install Dependencies**: Ensure you have Python installed on your system along with the required libraries. You can install the necessary libraries using pip:
    ```bash
    pip install -r requirements.txt
    ```
2. **Obtain API Key**: Sign up for an account at [Football Data API](https://www.football-data.org/) and obtain your API key.
3. **Update API Key in Script**: Open the `project.py` file and replace the placeholder API key with your own:
    ```python
    API_KEY = {"X-Auth-Token": "your_actual_api_key"}
    ```
4. **Run the Application**: Use the following commands to fetch and display information:
    ```bash
    python project.py -t <LEAGUE_ID>  # To get the league table
    python project.py -m <LEAGUE_ID>  # To get upcoming matches
    python project.py -s <LEAGUE_ID>  # To get top scorers
    ```
   Replace `<LEAGUE_ID>` with the appropriate league identifier:
   - `PD` for Primera Division
   - `SA` for Serie A
   - `PL` for Premier League
   - `BL1` for Bundesliga
   - `FL1` for Ligue 1
   - `CL` for Champions League

### Project Structure:
- **project.py**: The main script that handles command-line arguments and orchestrates the retrieval and display of league information.
- **test_project.py**: Contains test functions to ensure the core functionalities of `fetch_data`, `get_targeted_data`, and `get_headers` are working as expected.
- **requirements.txt**: Lists the required dependencies (`requests`, `tabulate`, `colorama`) to run the project.

### Testing:
- **test_project.py**:
    - **Purpose**: Contains test functions to verify the correctness of fetch_data, get_targeted_data, and get_headers. Uses pytest for testing, ensuring each function behaves as expected and handles various scenarios appropriately. The tests include checking the structure of the API response and validating the extracted data and headers.
    - **How to run**:
    ```bash
    pytest test_project.py
    ```

### Example Usage:
```bash
python project.py -t PL  # Get the Premier League table
python project.py -m CL  # Get upcoming matches in the Champions League
python project.py -s SA  # Get top scorers in Serie A
```



