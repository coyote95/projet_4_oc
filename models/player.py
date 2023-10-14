from datetime import date
from tinydb import TinyDB, Query


class Player:
    def __init__(self, name, surname, birthday, id_chess="AB12345"):
        self._name = name
        self._surname = surname
        self._birthday = birthday
        self.id_chess = id_chess

    def save_player_to_json(self, player):
        db = TinyDB("test.json")
        db.insert(player.dictionnary_player())

    def dictionnary_player(self):
        return {"name": self._name, "surname": self._surname, "birtday": self._birthday.isoformat(),
                "id_chess": self.id_chess}
