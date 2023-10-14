main.py

from models.player import Player
from controllers.player_controllers import PlayerController
from datetime import date

player1 = Player("Dupont", "Adrien", date(1990, 5, 15), 50)
player2 = Player("Moline", "Séverine", date(1992, 2, 1), 500)
player3 = Player("Kagon", "Nino", date(1988, 11, 4), 350)
player4 = Player("Guyot", "Maxime", date(1998, 3, 27), 400)
player5 = Player("Dalco", "Lucien", date(1995, 8, 12), 500)
player6 = Player("Vardie", "Jennifer", date(1995, 7, 21), 275)
player7 = Player("Dupont", "Adrien", date(1990, 5, 15), 50)

controller = PlayerController(Player)
filename = "test.json"
controller.add_player_controller(filename, player1)


player.py

from datetime import date
from tinydb import TinyDB, Query


class Player:
    def __init__(self, name, surname, birthday, id_chess="AB12345"):
        self._name = name
        self._surname = surname
        self._birthday = birthday
        self.id_chess = id_chess

    @staticmethod
    def add_player(self, filename, player):
        db = TinyDB(filename)
        db.insert(player.dictionnary_player())


    def dictionnary_player(self):
        return {"name": self._name, "surname": self._surname, "birtday": self._birthday.isoformat(),
                "id_chess": self.id_chess}




player_controllers.py


class PlayerController:
    def __init__(self,model):
        self.model=model

    def add_player_controller(self, filename,player):
        self.model.add_player(filename,player)






