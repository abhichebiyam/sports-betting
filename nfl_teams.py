import requests 


class NFL_Teams:

    def __init__(self):
        self.API_KEY = "d55f4a9313ea872d66f4c28bd4edd54f"
        self.sport = "americanfootball_nfl"

        self.sports_params = {
            "apiKey": self.API_KEY
        }

        self.nfl_games_params = {
            "sport": "americanfootball_nfl",
            "apiKey": self.API_KEY
        }

        self.nfl_game_odds_params = {
            "apiKey": self.API_KEY,
            "regions": "us",
            "markets": "h2h",
            "oddsFormat": "american"
        }

        self.game_ids = []
        self.all_teams = []
    
    def getRequestsLeft(self):
        sports_response = requests.get("https://api.the-odds-api.com/v4/sports", params=self.sports_params)
        headers = sports_response.headers

        # Extract specific headers
        requests_remaining = headers.get("x-requests-remaining")
        requests_used = headers.get("x-requests-used")
        requests_last = headers.get("x-requests-last")

        # Print the extracted headers
        print(f"Requests Remaining: {requests_remaining}")
        print(f"Requests Used: {requests_used}")
        print(f"Last Request Cost: {requests_last}")
    
    def getThisWeeksNFLGames(self):

        url = f"https://api.the-odds-api.com/v4/sports/{self.sport}/events"

        nfl_games_response = requests.get(url, params=self.nfl_games_params)
        nfl_games_data = nfl_games_response.json()

        for game in nfl_games_data:
            self.all_teams.append(game["home_team"])
            self.all_teams.append(game["away_team"])
            self.game_ids.append(game["id"])

            print(game["home_team"], "vs", game["away_team"])
            print("id: " + game["id"])
        
        self.getOddsForEachGame()
    
    def getOddsForEachGame(self):

        for id in self.game_ids:
            url = f"https://api.the-odds-api.com/v4/sports/{self.sport}/events/{id}/odds"
            nfl_game_odds_response = requests.get(url, params=self.nfl_game_odds_params)
            nfl_game_odds_data = nfl_game_odds_response.json()
            print(nfl_game_odds_data['bookmakers'][1])

