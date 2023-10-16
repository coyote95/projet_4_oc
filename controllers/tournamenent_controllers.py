class TournamentController:

    def __init__(self,model,view):
        self.model = model
        self.view= view

    def display_player_controller(self):
        print("Liste des participants au tournoi:")
        self.view.display_players_tournament(self.model)


    def add_tournament_player_controller(self, player):
        self.model.add_tournament_player(player)

    # def get_players(self):
    #     return self.tournament.saving_players
    #
    # def add_tournament_controllers(self, tournament):
    #     self.tournament.append(tournament)
