class TournamentView:
    def __init__(self, tournament):
        self.tournament = tournament

    def display_players_tournament(self):
        print("******** Affichage des participants au tournoi ******  ")
        for item in self.tournament.get_tournament_players():
            print(item)
            # for key, value in item.items():
            #     print(f'{key}:\t{value}')



