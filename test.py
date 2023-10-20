from models.player import Player
from models.tournament import Tournament
from models.menu import MenuEntry, Menu
from models.round import Round
from models.match import Match
from views.player_view import PlayerView
from views.tournament_view import TournamentView
from views.menu_view import HomeMenuView
from views.round_view import RoundView
from views.match_view import MatchView
from controllers.player_controllers import PlayerController
from controllers.tournamenent_controllers import TournamentController
from controllers.menu_controllers import ApplicationController, HomeMenuController, MenuNewTournamentController
from controllers.round_controllers import RoundController
from controllers.match_controllers import MatchController

from datetime import date, timedelta
from tinydb import TinyDB, Query
round=Round()
list=[]
player1 = Player("Dupont", "Adrien", date(1990, 5, 15), 50)
list.append(player1)
round.matchs.append(player1)
player1.set_name("julien")
round.matchs.append(player1)
list.append(player1)
print(round.matchs)
print(list)



player1 = Player("Marcel", "Marcel", date(1990, 5, 15), 50)
for i in range(0):
    player1=Player(f"Marcel{i}", "Marcel", date(1990, 5, 15), 50)
    list.append(player1)
    round.matchs.append(player1)
print(list)
print(round.matchs)

# list=[]
# player1=5
# list.append(player1)
# player1=10
# list.append(player1)
# print(list)