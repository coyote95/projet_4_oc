from views.player_view import PlayerView
from models.player import Player, NewPlayer
from datetime import date


class PlayerController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add_player(self, player):
        self.model.add_player(player)

    def save_players_to_json(self, filename):
        self.model.save_to_json(filename)

    def display_players(self):
        players = self.model.get_players()
        self.view.display_players(players)




if __name__ == "__main__":
    # Créer les instances de Player
    player1 = Player("Dupont", "Adrien", date(1990, 5, 15), 50)
    player2 = Player("Moline", "Séverine", date(1992, 2, 1), 500)
    player3 = Player("Kagon", "Nino", date(1988, 11, 4), 350)
    player4 = Player("Guyot", "Maxime", date(1998, 3, 27), 400)
    player5 = Player("Dalco", "Lucien", date(1995, 8, 12), 500)
    player6 = Player("Vardie", "Jennifer", date(1995, 7, 21), 275)

    # Créer le modèle, la vue et le contrôleur
    model = NewPlayer()
    view = PlayerView()
    controller = PlayerController(model, view)

    # Ajouter les joueurs au modèle
    controller.add_player(player1)
    controller.add_player(player2)
    controller.add_player(player3)
    controller.add_player(player4)
    controller.add_player(player5)
    controller.add_player(player6)

    # Enregistrer les joueurs dans un fichier JSON
    controller.save_players_to_json("joueurs.json")

    # Afficher les joueurs
    controller.display_players()
