from models.round import Round
from views.round_view import RoundView


class RoundController:

    def __init__(self, round):
        self.model = round
        self.view = RoundView(self.model)

    def creation_round(self, tournament):
        round = tournament.get_numbers_round()
        for tour in range(round):
            print(f"round n° {tour}")

    def display_round_controler(self):
        self.view.display_round()
