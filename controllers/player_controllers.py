from views.player_view import PlayerView
from models.player import Player
from datetime import date
import json


class PlayerHandlerController:
    def __init__(self):
        self._players = []

    def add_player(self, player):
        self._players.append(player)

    def __contains__(self, player):
        return player in self._players

    def __iter__(self):
        return iter(self._players)



    def get_players(self):
        return self._players

    def save_to_json(self, filename):
        players_date = [player.dictionnary_player() for player in self._players]  # modifier avec contain
        with open(filename, "w") as json_file:
            json.dump(players_date, json_file, indent=4)

    def display_players(self):
        players = self.get_players()
        view = PlayerView()
        view.display_players(players)


if __name__ == "__main__":
    # Créer les instances de Player
    player1 = Player("Dupont", "Adrien", date(1990, 5, 15), 50)
    player2 = Player("Moline", "Séverine", date(1992, 2, 1), 500)
    player3 = Player("Kagon", "Nino", date(1988, 11, 4), 350)
    player4 = Player("Guyot", "Maxime", date(1998, 3, 27), 400)
    player5 = Player("Dalco", "Lucien", date(1995, 8, 12), 500)
    player6 = Player("Vardie", "Jennifer", date(1995, 7, 21), 275)

    handler = PlayerHandlerController()
    handler.add_player(player1)
    handler.add_player(player2)

    handler.display_players()
    handler.save_to_json("joueurs.json")
    if player1 in handler:
        print("true")
    else:
        print("false")

    for player in handler:
        print(player)
