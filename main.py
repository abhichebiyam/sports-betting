import nfl_teams as teams
import nfl_database as database

team_instance = teams.NFL_Teams()
database_instance = database.NFL_Database()

print()
team_instance.getRequestsLeft()
print()
team_instance.getThisWeeksNFLGames()