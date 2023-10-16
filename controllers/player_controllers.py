class PlayerController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def save_player_controller(self, filename):
        self.model.save_player_to_json(filename)

    def display_db(self,filename):
        self.view.view_player_bd(filename)

if __name__ == "__main__":
    from views.player_view import PlayerView
    from models.player import Player
    from datetime import date

    player1 = Player("Guillot", "Aurore", date(1990, 5, 15), 50)

    model = player1
    view = PlayerView()
    controller = PlayerController(model, view)
    controller.save_player_controller("test2.json")
    controller.display_db("test2.json")

