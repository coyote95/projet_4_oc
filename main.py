from models.player import Player
from models.tournament import Tournament
from views.player_view import PlayerView
from views.tournament_view import TournamentView
from controllers.player_controllers import PlayerController
from controllers.tournamenent_controllers import TournamentController

from datetime import date, timedelta
from tinydb import TinyDB, Query


player1 = Player("Dupont", "Adrien", date(1990, 5, 15), 50)
player2 = Player("Moline", "Séverine", date(1992, 2, 1), 500)
player3 = Player("Kagon", "Nino", date(1988, 11, 4), 350)
player4 = Player("Guyot", "Maxime", date(1998, 3, 27), 400)
player5 = Player("Dalco", "Lucien", date(1995, 8, 12), 500)
player6 = Player("Vardie", "Jennifer", date(1995, 7, 21), 275)
player7 = Player("Dupont", "Adrien", date(1990, 5, 15), 50)

db = TinyDB("Players.json")
db.truncate()

view = PlayerView()

controller = PlayerController(player1, view)
controller.save_player_controller("Players.json")
controller.display_player_controller()

controller = PlayerController(player2, view)
controller.save_player_controller("Players.json")
controller.display_player_controller()

controller = PlayerController(player3, view)
controller.save_player_controller("Players.json")
controller.display_player_controller()

controller = PlayerController(player4, view)
controller.save_player_controller("Players.json")
controller.display_player_controller()

controller.display_db("Players.json")



#######TOURNOI###
date_start = date(2023, 10, 14)
date_end = date_start + timedelta(4)
Championnat = Tournament("championnat académique", "Cergy", date_start, date_end)
print(Championnat)

model=Championnat
view = TournamentView()
controller = TournamentController(model, view)
controller.add_tournament_player_controller(player1)
controller.add_tournament_player_controller(player2)

controller.display_player_controller()

    # controller_tournoi.add_tournament_player(player1)
    # controller_tournoi.add_tournament_player(player2)
    # controller_tournoi.add_tournament_player(player3)
    # controller_tournoi.add_tournament_player(player4)
    #
    # controller_tournoi.display_player_controller()

