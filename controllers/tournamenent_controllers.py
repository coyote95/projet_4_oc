class TournamentController:

    def __init__(self, model, view):
        self.model = model
        self.view = view

    def display_player_controller(self):
        print("Liste des participants au tournoi:")
        self.view.display_players_tournament()

    def add_tournament_player_controller(self, player):
        self.model.add_tournament_player(player)

    def dialogue(self):
        name=input("Non du tournoi:")
        self.model.new_name(name)