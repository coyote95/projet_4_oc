class MatchView:
    def __init__(self, match):
        self.match = match

    def display_match(self):
        print("*************    Affichage du match    *************")
        print(f"{self.match.player1.name} {self.match.player1.surname} "
              f"(Joueur1: {self.match.player1.color})"
              f"   contre   "
              f"{self.match.player2.name} {self.match.player1.surname} "
              f"(Joueur2: {self.match.player2.color})")

    @staticmethod
    def input_name():
        print("Nom du tournoi:")
        name = input(">>")
        return name
