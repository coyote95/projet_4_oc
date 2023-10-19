from models.match import Match
from views.match_view import MatchView


class MatchController:

    def __init__(self, match):
        self.model = match
        self.view = MatchView(self.model)

    def display_match_controler(self):
        self.view.display_match()
