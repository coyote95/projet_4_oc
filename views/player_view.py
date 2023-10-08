class PlayerView:
    def display_players(self,players):
        for player in players:
            print(f"Nom:{player.name} \t Prénom: {player.surname}")