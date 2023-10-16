class TournamentView:

    def display_players_tournament(self,tournament):
        print("Affichage des participants au tournoi :")
        for player in tournament.get_tournament_players():
            print(player)
