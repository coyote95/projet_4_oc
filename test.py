player.py


class Player:
    def __init__(self, name, surname, birthday, id_chess="AB12345"):
        self._name = name
        self._surname = surname
        self._birthday = birthday
        self.id_chess = id_chess

    def save_player_to_json(self, filename):
        db = TinyDB(filename)
        db.insert(self.dictionnary_player())

    def get_filename(self):
        return self.filename

    def dictionnary_player(self):
        return {"name": self._name, "surname": self._surname, "birthday": self._birthday.isoformat(),
                "id_chess": self.id_chess}

player_view.py

class PlayerView:
    def __init__(self):
        self.player=player

    def view_player_bd(self,filename):
        db = TinyDB(filename)
        all_items = db.all()
        for item in all_items:
            print(item)

    def display_player(self):
        print (self.player.dictionnary_player())

player_controllers.py

class PlayerController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def save_player_controller(self, filename):
        self.model.save_player_to_json(filename)

    def display_db(self,filename):
        self.view.view_player_bd(filename)

    def display_player_controller(self):
        self.view.display_player(self)

if __name__ == "__main__":
    from views.player_view import PlayerView
    from models.player import Player
    from datetime import date

    player1 = Player("Guillot", "Aurore", date(1990, 5, 15), 50)
    model = player1
    view = PlayerView()
    controller= PlayerController(model, view)
    controller.save_player_controller("test2.json")
    controller.display_db("test2.json")
    print("attention")
    controller.save_player_controller()
