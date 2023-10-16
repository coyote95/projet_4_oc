# from models.player import Player
# from datetime import date
from tinydb import TinyDB, Query


class PlayerView:

    def view_player_bd(self,filename):
        db = TinyDB(filename)
        all_items = db.all()
        for item in all_items:
            print(item)


if __name__ == "__main__":
    from datetime import date
    from models.player import Player
    from tinydb import TinyDB, Query

    player1 = Player("Guillot", "Aurore", date(1990, 5, 15), 50)
    player1.save_player_to_json()
    PlayerView.view_player_bd
