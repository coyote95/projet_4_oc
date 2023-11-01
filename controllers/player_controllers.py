from views.player_view import PlayerView


class PlayerController:
    def __init__(self, player):
        self.model = player
        self.view = PlayerView()

    def save_player_controller(self, filename="./data/all_players.json",
                               score=True):
        self.model.save_player_to_json(filename, score)

    def display_db(self, filename):
        self.view.view_player_bd(filename)

    def display_player_controller(self):
        self.view.display_player(self.model)

    def creation_player(self):
        name = self.view.input_name()
        self.model.set_name(name)
        surname = self.view.input_surname()
        self.model.set_surname(surname)
        birthday = self.view.input_birthday()
        self.model.set_birthday(birthday)
        numero_id = self.view.input_id()
        self.model.set_id(numero_id)
