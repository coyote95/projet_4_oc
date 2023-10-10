class PlayerView:

    def __init__(self,players):
        self.players = players

    def display_players(self):
        print("Affichage Joueurs:")
        for player in self.players:
            print(player)


