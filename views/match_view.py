class MatchView:
    def __init__(self, match):
        self.match = match

    def display_match(self):
        print("******** Affichage du match ******  ")
        print(f"Joueur 1:{self.match.player1}(score:{self.match.score1}" 
              f"VS"
              f"Joueur 2:{self.match.player}(score:{self.match.score2}" )

    def input_name(self):
        print("Nom du tournoi:")
        name = input(">>")
        return name

