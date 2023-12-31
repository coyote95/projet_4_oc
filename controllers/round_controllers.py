from views.round_view import RoundView


class RoundController:
    def __init__(self, round_game):
        self.model = round_game
        self.view = RoundView(self.model)

    def get_match_controller(self):
        return self.model.get_match()

    def increment_numero_round_controller(self):
        self.model.increment_numero_round()

    def add_match_controller(self, match):
        self.model.add_match(match)

    def display_round_controller(self):
        self.view.display_round()

    def display_match_controller(self):
        self.view.display_match()

    def display_match_players_controller(self):
        self.view.display_match_players()

    def set_numero_controller(self, num):
        self.model.set_numero(num)

    def set_date_save_controller(self, date):
        self.model.set_date_save(date)

    def save_round_to_json_controller(self, filename="./data/rounds.json"):
        self.model.save_round_to_json(filename)

    def save_match_round_to_json_controller(self, filename="./data/rounds.json"):
        self.model.save_match_round_to_json(filename)
