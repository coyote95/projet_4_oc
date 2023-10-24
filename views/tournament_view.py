import controllers.menu_controllers
# from controllers.menu_controllers import ApplicationController


class TournamentView:
    def __init__(self, tournament):
        self.tournament = tournament

    def display_players_tournament(self):
        print(f"******** Affichage des participants au tournoi ****** ")
        for item in self.tournament.get_tournament_players():
            print(item)

    def display_tournament_info(self):
        print(f"*********Tournoi*******\n"
              f"Nom: {self.tournament.name}: \n"
              f"Place: {self.tournament.place}\n"
              f"Date de debut: {self.tournament.date_end}\n"
              f"Date de fin: {self.tournament.date_end}\n"
              f"Nombre de round total:{self.tournament.numbers_round}\n"
              # f"Nombre de participants:{self.tournament.nombre_de_participants()}"
              )

    def display_numero_round(self):
        print(f'************************Round numero {self.tournament.actual_round}***************\n')

    def input_name(self):
        print("Nom du tournoi:")
        name = input(">>")
        return name

    def input_place(self):
        print("lieu du tournoi:")
        place = input(">>")
        return place

    def input_date_start(self):
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

    def input_date_end(self):
        while True:
            print("Date de fin du tournoi (dd-mm-yyyy):")
            end_date = input(">>")
            try:
                jour, mois, annee = map(int, end_date.split('-'))
                if 1 <= jour <= 31 and 1 <= mois <= 12 and 1900 <= annee:
                    return end_date
                else:
                    print(
                        "La date saisie est invalide")
            except ValueError:
                print("Format invalide. Assurez-vous de séparer la date par des tirets (dd-mm-yyyy).")

    def input_number_round(self):
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
