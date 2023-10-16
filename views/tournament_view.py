class TournamentView:
    def __init__(self,tournament):
        self.tournament = tournament



    def display_players_tournament(self):
        print("Affichage des participants au tournoi :")
        for player in self.tournament.get_tournament_players():
            print(player)



