from datetime import date
from tinydb import TinyDB, Query


class Player:
    def __init__(self, name, surname, birthday, id_chess="AB12345"):
        self._name = name
        self._surname = surname
        self._birthday = birthday
        self.id_chess = id_chess

    def save_player_to_json(self):
        db = TinyDB("test.json")
        db.insert(self.dictionnary_player())

    def dictionnary_player(self):
        return {"name": self._name, "surname": self._surname, "birtday": self._birthday.isoformat(),
                "id_chess": self.id_chess}

    def view_player_bd():
        db =TinyDB("test.json")
        all_items= db.all()
        for item in all_items:
            print(item)

if __name__ == "__main__":


     player1=Player("Guillot", "Aurore", date(1990, 5, 15), 50)
     player1.save_player_to_json()
     Player.view_player_bd()

