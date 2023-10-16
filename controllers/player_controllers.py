from views.player_view import PlayerView
from models.player import Player
from datetime import date


class PlayerController:
    def __init__(self):
        pass

    def save_player_controller(self, player):
        Player.save_player_to_json()
