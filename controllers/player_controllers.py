from views.player_view import PlayerView
from models.player import Player
from datetime import date


class PlayerController:
    def __init__(self, player):
        self.player = player

    def save_player_controller(self):
        self.player.save_player_to_json(self.player)
