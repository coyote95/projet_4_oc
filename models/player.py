from tinydb import TinyDB, Query


class Player:
    def __init__(self, name, surname, birthday, id_chess="AB12345"):
        self._name = name
        self._surname = surname
        self._birthday = birthday
        self.id_chess = id_chess

    def __str__(self):
        return (
            f"*********Player*******\n"
            f" Nom: {self._name}: \n"
            f" Surname: {self._surname}\n"
          )

    def save_player_to_json(self, filename):
        db = TinyDB(filename)
        db.insert(self.dictionnary_player())

    def get_name(self):
        return self._name

    def get_surname(self):
        return self._surname

    def get_birthday(self):
        return self._birthday

    def get_id_chess(self):
        return self.id_chess

    def dictionnary_player(self):
        return {"name": self._name, "surname": self._surname, "birthday": self._birthday.isoformat(),
                "id_chess": self.id_chess}


    def new_name(self,name):
        self._name=name

    def new_surname(self,surname):
        self._surname=surname

    def new_birthday(self,birthday):
        self._birthday=birthday

    def new_id(self,id_chess):
        self.id_chess=id_chess




# if __name__ == "__main__":
#     from datetime import date
#     from tinydb import TinyDB, Query
#     from views import player_view
#
#     player1 = Player("Guillot", "Aurore", date(1990, 5, 15), 50)
#     player1.save_player_to_json()
#     Player.view_player_bd()
