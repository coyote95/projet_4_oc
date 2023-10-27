from models.round import Round
from views.round_view import RoundView


class RoundController:

    def __init__(self, round):
        self.model = round
        self.view = RoundView(self.model)

    def get_match_controller(self):
        return self.model.get_match()

    def creation_round(self, tournament):
        round = tournament.get_numbers_round()
        for tour in range(round):
            print(f"round n° {tour}")

    def add_match_controller(self, match):
        self.model.add_match(match)

    def display_round_controler(self):
        self.view.display_round()

    def display_match_controller(self):
        self.view.display_match()

    def set_numero_controller(self, num):
        self.model.set_numero(num)

    def set_commence_controller(self, commence):
        self.model.set_commence(commence)

    def set_termine_controller(self, termine):
        self.model.set_termine(termine)

    def save_round_to_json_controller(self, filename="./data/rounds.json"):
        self.model.save_round_to_json(filename)
