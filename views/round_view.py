class RoundView:
    def __init__(self, game_round):
        self.game_round = game_round

    def display_round(self):
        print("******** Affichage du round ******  ")
        print(
            f"Round name:{self.game_round.name}\n"
            f"Numero du round:{self.game_round.numero_round}\n"
            f"Date d'enregistrement du round:{self.game_round.date_save}\n"
        )
        for match in self.game_round.matchs:
            print(match)

    def display_match_players(self):
        print("Affichage des matchs")
        i = 1
        for item in self.game_round.matchs:
            print(
                f"Match {i}:  {item.player1.name} {item.player1.surname}"
                f" (joueur1: {item.player1.color})    contre    "
                f"{item.player2.name} {item.player2.surname} "
                f"(joueur2: {item.player2.color}) "
            )
            i += 1
        print()

    def display_match(self):
        print("Affichage des matchs")
        i = 1
        for item in self.game_round.matchs:
            print(f"Match {i}:  {item}")
            i += 1
        print()
