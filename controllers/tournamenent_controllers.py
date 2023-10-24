import views.tournament_view
from models.tournament import Tournament


# rom views.tournament_view import TournamentView


class TournamentController:

    def __init__(self, tournament):
        self.model = tournament
        self.view = views.tournament_view.TournamentView(self.model)

    def display_player_tournament_controler(self):
        self.view.display_players_tournament()

    def display_tournament_info_controler(self):
        self.view.display_tournament_info()

    def add_tournament_player_controller(self, player):
        self.model.add_tournament_player(player)

    def add_list_tournament_round_controller(self, round):
        self.model.add_list_tournament_round(round)

    def increment_actual_round_controller(self):
        self.model.increment_numbers_round()

    def creation_tournoi(self):
        name = self.view.input_name()
        self.model.set_name(name)
        place = self.view.input_place()
        self.model.set_place(place)
        start_date = self.view.input_date_start()
        self.model.set_date_start(start_date)
        end_date = self.view.input_date_end()
        self.model.set_date_end(end_date)
        number_round = int(self.view.input_number_round())
        self.model.set_round(number_round)

    def get_name_controller(self):
        return self.model.get_name()

    def input_number_players_controller(self):
        return self.view.input_number_players()

    def save_player_tournament_to_json_controller(self,filename, table_name="players"):
        self.model.save_player_tournament_to_json(filename, table_name)

    def save_tournament_info_to_json_controller(self, filename, table_name="save_info"):
        self.model.save_tournament_info_to_json(filename, table_name)
