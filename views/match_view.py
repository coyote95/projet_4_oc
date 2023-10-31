class MatchView:
    def __init__(self, match):
        self.match = match

    def display_match(self):
        print("*************    Affichage du match    *************")
        print(f"{self.match.player1.name} {self.match.player1.surname} (Joueur1)"
              f"   contre   "
              f"{self.match.player2.name} {self.match.player1.surname} (Joueur2)")

    @staticmethod
    def input_name():
        print("Nom du tournoi:")
        name = input(">>")
        return name
