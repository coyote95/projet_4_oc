player.py

from tinydb import TinyDB, Query


class Player:
    def __init__(self, name, surname, birthday, id_chess="AB12345"):
        self._name = name
        self._surname = surname
        self._birthday = birthday
        self.id_chess = id_chess
        self.filename = "test.json"

    def save_player_to_json(self):
        db = TinyDB(self.filename)
        db.insert(self.dictionnary_player())

    def get_filename(self):
        return self.filename

    def dictionnary_player(self):
        return {"name": self._name, "surname": self._surname, "birthday": self._birthday.isoformat(),
                "id_chess": self.id_chess}

player_view.py


class PlayerView:

    def __init__(self,player=None):
        self.player = player

    def view_player_bd(self):
        db = TinyDB(self.filename)
        all_items = db.all()
        for item in all_items:
            print(item)


if __name__ == "__main__":
    from datetime import date
    from models.player import Player
    from tinydb import TinyDB, Query

    player1 = Player("Guillot", "Aurore", date(1990, 5, 15), 50)
    player1.save_player_to_json()
    PlayerView.view_player_bd()
