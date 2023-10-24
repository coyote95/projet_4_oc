class TournamentView:
    def __init__(self, tournament):
        self.tournament = tournament

    def display_players_tournament(self):
        print(f"******** Affichage des participants au tournoi ****** ")
        for item in self.tournament.get_tournament_players():
            print(item)
            # for key, value in item.items():
            #     print(f'{key}:\t{value}')

    def display_tournament_info(self):
        print(f"*********Tournoi*******\n"
              f"Nom: {self.tournament.name}: \n"
              f"Place: {self.tournament.place}\n"
              f"Date de debut: {self.tournament.date_end}\n"
              f"Date de fin: {self.tournament.date_end}\n"
              f"Nombre de round total:{self.tournament.numbers_round}\n"
             # f"Nombre de participants:{self.tournament.nombre_de_participants()}"
              )

    def input_name(self):
        print("Nom du tournoi:")
        name = input(">>")
        return name

    def input_place(self):
        print("lieu du tournoi:")
        place = input(">>")
        return place

    def input_date_start(self):
        print("Date de debut du tournoi(aaaa,mm,jj):")
        start_date = input(">>")
        return start_date

    def input_date_end(self):
        print("Date de fin du tournoi(aaaa,mm,jj):")
        end_date = input(">>")
        return end_date

    def input_number_round(self):
        print("Nombre de round:")
        while True:
            try:
                number_round = input(">>")
                entier = int(number_round)
                break
            except ValueError:
                print("L'entrée n'est pas un entier.")
        return number_round

    def input_number_players(self):
        while True:
            print("Nombre de joueurs au tournoi:")
            try:
                nombre_participant = input(">>")
                entier = int(nombre_participant)
                return entier
            except ValueError:
                print("L'entrée n'est pas un entier.")


