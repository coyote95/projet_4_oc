class MatchView:
    def __init__(self, match):
        self.match = match

    def display_match(self):
        print("******** Affichage du match ********  ")
        print(f"Joueur 1:{self.match.player1} "
              f"CONTRE "
              f"Joueur 2:{self.match.player2}")

    @staticmethod
    def input_name():
        print("Nom du tournoi:")
        name = input(">>")
        return name
