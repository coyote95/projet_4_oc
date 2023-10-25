import views.tournament_view
from models.tournament import Tournament


# rom views.tournament_view import TournamentView


class TournamentController:

    def __getitem__(self, choice):  # tournament[0]
        return self.model[choice]

    def __init__(self, tournament):
        self.model = tournament
        self.view = views.tournament_view.TournamentView(self.model)

    def display_player_tournament_controler(self):
        self.view.display_players_tournament()

    def display_tournament_info_controler(self):
        self.view.display_tournament_info()

    def display_actual_numero_round_controller(self):
        self.view.display_numero_round()

    def nombre_de_participant_pair_controller(self):
        self.model.nombre_de_participant_pair()

    def nombre_de_participants_controller(self):
        return self.model.nombre_de_participants()

    def add_tournament_player_controller(self, player):
        self.model.add_tournament_player(player)

    def add_list_tournament_round_controller(self, round):
        self.model.add_list_tournament_round(round)

    def increment_actual_round_controller(self):
        self.model.increment_actual_round()

    def creation_tournoi(self):
        name = self.view.input_name()
        self.model.set_name(name)
        place = self.view.input_place()
        self.model.set_place(place)
        # start_date = self.view.input_date_start()
        # self.model.set_date_start(start_date)
        # end_date = self.view.input_date_end()
        # self.model.set_date_end(end_date)
        number_round = int(self.view.input_number_round())
        self.model.set_round(number_round)

    def get_name_controller(self):
        return self.model.get_name()

    def input_number_players_controller(self):
        return self.view.input_number_players()

    def save_player_tournament_to_json_controller(self, filename="./data/tournaments.json"):
        self.model.save_player_tournament_to_json(filename)

    def save_tournament_info_to_json_controller(self, filename="./data/tournaments.json"):
        self.model.save_tournament_info_to_json(filename)

    def save_round_tournament_to_json_controller(self, filename, table_name="round"):
        self.model.save_round_tournament_to_json(filename, table_name)

    def sort_players_by_score_controller(self):
        self.model.sort_players_by_score()

    def score_player_tournament_controller(self):
        for personne in range(0, len(self.model)):
            print(self.model[personne])
            print(self.model[personne].score)
