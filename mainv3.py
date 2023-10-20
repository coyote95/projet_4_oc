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


player1 = Player("Dupont", "Adrien", date(1990, 5, 15), 50)
player2 = Player("Moline", "Séverine", date(1992, 2, 1), 500)
player3 = Player("Kagon", "Nino", date(1988, 11, 4), 350)
player4 = Player("Guyot", "Maxime", date(1998, 3, 27), 400)
# player5 = Player("Dalco", "Lucien", date(1995, 8, 12), 500)
# player6 = Player("Vardie", "Jennifer", date(1995, 7, 21), 275)
# player7 = Player("Dupont", "Adrien", date(1990, 5, 15), 50)

# #*********************     TOURNOI     **************************
date_start = date(2023, 10, 14)
date_end = date_start + timedelta(4)
championnat = Tournament("championnat académique", "Cergy", date_start, date_end, 6)
controller_tournoi = TournamentController(championnat)

controller_tournoi.add_tournament_player_controller(player1)
controller_tournoi.add_tournament_player_controller(player2)
controller_tournoi.add_tournament_player_controller(player3)
controller_tournoi.add_tournament_player_controller(player4)
# controller_tournoi.add_tournament_player_controller(player5)
# controller_tournoi.add_tournament_player_controller(player6)

controller_tournoi.display_tournament_info_controler()
controller_tournoi.display_player_tournament_controler()

championnat.save_player_tournament_to_json()

db=TinyDB(r'C:\Users\Ghost\OneDrive\Documents\Openclassrooms\Projet_4\chess_tournaments\tournoi\players.json')
print()
doc_id_to_find = 1

# Utilisez une requête TinyDB pour rechercher l'enregistrement par "doc_id"
Record = Query()
result = db.get(Record.doc_id == doc_id_to_find)

