import controllers.menu_controllers


class TournamentView:
    def __init__(self, tournament):
        self.tournament = tournament

    def __call__(self, *args, **kwargs):
        self.display_tournament_info()
        self.display_players_tournament()
        self.display_round_tournament()

    def display_players_tournament(self):
        print(f"********     Affichage des participants au tournoi      ****** ")
        for item in self.tournament.get_tournament_players():
            print(item)

    def display_round_tournament(self):
        print(f"********     Affichage des rounds du tournoi    ******** ")
        for item in self.tournament.get_list_rounds():
            print(item)

    def display_tournament_info(self):
        print(f"***************     Tournoi     *********\n"
              f"Nom: {self.tournament.name}: \n"
              f"Place: {self.tournament.place}\n"
              f"Date de debut: {self.tournament.date_end}\n"
              f"Date de fin: {self.tournament.date_end}\n"
              f"Nombre de round total:{self.tournament.numbers_round}"
              )

    def display_numero_round(self):
        print()
        print(f'************************ Round numero {self.tournament.actual_round} ***************\n')

    def display_end_tournament(self):
        print()
        print(f'************************ Fin du Tournoi ***************\n')
        self.display_tournament_info()
        self.display_players_tournament()
        self.display_round_tournament()
        print()

    @staticmethod
    def input_name():
        print("Nom du tournoi:")
        name = input(">>")
        return name

    @staticmethod
    def input_place():
        print("lieu du tournoi:")
        place = input(">>")
        return place

    @staticmethod
    def input_date_start():
        while True:
            print("Date de debut du tournoi (dd-mm-yyyy):")
            start_date = input(">>")
            try:
                jour, mois, annee = map(int, start_date.split('-'))
                if 1 <= jour <= 31 and 1 <= mois <= 12 and 1900 <= annee:
                    return start_date
                else:
                    print(
                        "La date saisie est invalide")
            except ValueError:
                print("Format invalide. Assurez-vous de séparer la date par des tirets (dd-mm-yyyy).")

    @staticmethod
    def input_date_end():
        while True:
            print("Date de fin du tournoi (dd-mm-yyyy):")
            end_date = input(">>")
            try:
                jour, mois, annee = map(int, end_date.split('-'))
                if 1 <= jour <= 31 and 1 <= mois <= 12 and 1900 <= annee:
                    return end_date
                else:
                    print("La date saisie est invalide")
            except ValueError:
                print("Format invalide. Assurez-vous de séparer la date par des tirets (dd-mm-yyyy).")

    @staticmethod
    def input_number_round():
        print("Nombre de round:")
        while True:
            try:
                number_round = input(">>")
                test = int(number_round)
                break
            except ValueError:
                print("L'entrée n'est pas un entier.")
        return number_round

    def input_number_players(self):
        while True:
            print("Nombre de joueurs au tournoi:")
            try:
                nombre_participant = input(">>")
                test = int(nombre_participant)
                break
            except ValueError:
                print("L'entrée n'est pas un entier.")

        for tentative in range(0, int(nombre_participant)):
            print(f"Player {tentative + 1}")
            app = controllers.menu_controllers.ApplicationController()
            app.player(self.tournament)

    def display_score_players(self):
        print("CLASSEMENT:")
        for personne in range(0, len(self.tournament)):
            print(f"{self.tournament[personne]} score: {self.tournament[personne].score}")


