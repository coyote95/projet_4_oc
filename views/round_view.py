class RoundView:
    def __init__(self, round):
        self.round = round

    def display_round(self):
        print("******** Affichage du round ******  ")
        print(f"Round name:{self.round.name}\n"
              f"Numero du round:{self.round.numero_round}\n"
              f"Debut du round:{self.round.commence}\n"
              f"Fin du round:{self.round.termine}")
        for match in self.round.matchs:
            print(match)

    def display_match(self):
        print("Affichage des matchs")
        i = 1
        for item in self.round.matchs:  # premier match
            print(f"Match {i}:  {item}")
            i += 1
        print()
