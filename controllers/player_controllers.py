class PlayerController:
    def __init__(self, player=None):
        self.player = player
        self.view = PlayerView(self.player)

    def save_player_controller(self):
        self.player.save_player_to_json()


if __name__ == "__main__":
    from views.player_view import PlayerView
    from models.player import Player
    from datetime import date

    player1 = Player("Guillot", "Aurore", date(1990, 5, 15), 50)
    PlayerController(player1).save_player_controller()


