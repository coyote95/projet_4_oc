class RoundView:
    def __init__(self, game_round):
        self.game_round = game_round

    def display_round(self):
        print("******** Affichage du round ******  ")
        print(f"Round name:{self.game_round.name}\n"
              f"Numero du round:{self.game_round.numero_round}\n"
              f"Date d'enregistrement du round:{self.game_round.date_save}\n")
        for match in self.game_round.matchs:
            print(match)

    def display_match(self):
        print("Affichage des matchs")
        i = 1
        for item in self.game_round.matchs:
            print(f"Match {i}:  {item}")
            i += 1
        print()
