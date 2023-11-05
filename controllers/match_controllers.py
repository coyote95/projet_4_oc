from views.match_view import MatchView


class MatchController:

    def __init__(self, match):
        self.model = match
        self.view = MatchView(self.model)

    def display_match_controller(self):
        self.view.display_match()

    def save_match_to_json_controller(self, filename="./data/matchs.json"):
        self.model.save_match_to_json(filename)

    def random_color_controller(self):
        self.model.random_color()

    def winner_controller(self,winning_player):
        self.model.winner(winning_player)
        self.view.display_winner(winning_player)
