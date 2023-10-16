from models.player import Player
from models.tournament import Tournament
from models.menu import MenuEntry, Menu
from views.player_view import PlayerView
from views.tournament_view import TournamentView
from views.menu_view import HomeMenuView
from controllers.player_controllers import PlayerController
from controllers.tournamenent_controllers import TournamentController
from controllers.menu_controllers import ApplicationController, HomeMenuController, MenuNewTournamentController

from datetime import date, timedelta
from tinydb import TinyDB, Query

########Menu
app = ApplicationController()
app.start()
menu = Menu()


newtournament = Tournament(None,None,None,None)


model = newtournament
view = TournamentView(model)  # appeler la vue du model
controller = TournamentController(model, view)
controller.dialogue()




####player
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

model = Championnat
view = TournamentView(model)  # appeler la vue du model
controller = TournamentController(model, view)
controller.add_tournament_player_controller(player1)
controller.add_tournament_player_controller(player2)

controller.display_player_controller()
