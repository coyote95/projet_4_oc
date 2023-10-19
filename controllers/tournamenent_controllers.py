from models.tournament import Tournament
from views.tournament_view import TournamentView


class TournamentController:

    def __init__(self, tournament):
        self.model = tournament
        self.view = TournamentView(self.model)

    def display_player_tournament_controler(self):
        self.view.display_players_tournament()

    def add_tournament_player_controller(self, player):
        self.model.add_tournament_player(player)

    def add_list_tournament_round_controller(self, round):
        self.model.add_list_tournament_round(round)

    def increment_actual_round_controller(self):
        self.model.increment_numbers_round()

    def creation_tournoi(self):
        print("Nom du tournoi:")
        name = input(">>")
        self.model.set_name(name)
        print("lieu du tournoi:")
        place = input(">>")
        self.model.set_place(place)
        print("Date de debut du tournoi(aaaa,mm,jj):")
        start_date = input(">>")
        self.model.set_date_start(start_date)
        print("Date de fin du tournoi(aaaa,mm,jj):")
        end_date = input(">>")
        self.model.set_date_end(end_date)
        print("Nombre de round:")
        numbers_date = input(">>")
        self.model.set_round(numbers_date)
