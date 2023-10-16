from models.player import Player
from views.player_view import PlayerView
from controllers.player_controllers import PlayerController
from datetime import date
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

