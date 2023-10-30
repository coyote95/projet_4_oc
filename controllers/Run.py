import controllers.menu_controllers
from models.player import Player
from models.tournament import Tournament
from models.menu import MenuEntry, Menu
from models.round import Round
from models.match import Match
from models.menu import Menu, MenuEntry
from views.player_view import PlayerView
# from views.tournament_view import TournamentView
from views.menu_view import HomeMenuView
from views.round_view import RoundView
from views.match_view import MatchView
from views.menu_view import HomeMenuView
from controllers.player_controllers import PlayerController
from controllers.tournamenent_controllers import TournamentController
from controllers.round_controllers import RoundController
from controllers.match_controllers import MatchController
# from controllers.menu_controllers import ApplicationController, HomeMenuController, PlayerMenuController
#    MenuListPlayersController, QuitController, Addplayer, ManuelPlayer

from datetime import date, timedelta, datetime
from tinydb import TinyDB, Query
import sys


class RunCreationTournoi:
    def __init__(self):
        self.tournament = Tournament(None, None, None, None)

    def __call__(self, *args, **kwargs):
        controller_tournoi = TournamentController(self.tournament)
        controller_tournoi.creation_tournoi()
        controller_tournoi.display_tournament_info_controler()
        controller_tournoi.input_number_players_controller()
        controller_tournoi.save_tournament_info_to_json_controller()
        controller_tournoi.save_player_tournament_to_json_controller()
        controller_tournoi.display_player_tournament_controler()
        run_instance = Run(self.tournament)
        run_instance()


class Run:
    def __init__(self, tournament):
        self.tournament = tournament

    def __call__(self, *args, **kwargs):
        controller_tournoi = TournamentController(self.tournament)

        for tour in range(self.tournament.get_numbers_round() - self.tournament.get_actual_round()):
            controller_tournoi.sort_players_by_score_controller()
            controller_tournoi.display_player_tournament_controler()

            controller_tournoi.increment_actual_round_controller()
            controller_tournoi.display_actual_numero_round_controller()

            round_tournament = Round()
            controller_round = RoundController(round_tournament)
            controller_round.set_numero_controller(controller_tournoi.get_actual_round_controller())
            controller_round.set_commence_controller(datetime.now().isoformat())

            app = controllers.menu_controllers.ApplicationController()
            app.ChoixJouerleRound(round_tournament)



            creation_pair_match_instance = CreationPairMatch(self.tournament, round_tournament)
            creation_pair_match_instance()

            #         ####################code #########################

            print("Affichage Gagnant:")

            for match in controller_round.get_match_controller():
                print(match)
                app = controllers.menu_controllers.ApplicationController()
                app.choixgagnantmatch(match)
                match.save_match_to_json()

            # *********************code***************

            controller_tournoi.add_list_tournament_round_controller(round_tournament)

            score_instance = UpdateScoreRun(self.tournament, round_tournament)
            score_instance()

            controller_tournoi.score_player_tournament_controller()

            controller_round.save_round_to_json_controller()
            controller_round.save_match_round_to_json_controller()
            controller_tournoi.save_round_tournament_to_json_controller()

            controller_round.set_termine_controller(datetime.now().isoformat())

        print(f"***********************Fin tournoi***************\n")

        for i in range(len(self.tournament.tournament_players)):
            print(self.tournament[i])

        for j in range(len(self.tournament.list_round)):
            print(self.tournament.list_round[j])

        print("listes de tous les matchs")
        for round_game in self.tournament.list_round:
            for match in round_game.matchs:
                print(match)


class UpdateScoreRun:
    def __init__(self, tournament, round_game):
        self.tournament = tournament
        self.round = round_game

    def __call__(self, *args, **kwargs):

        for match in self.round.matchs:
            for players in self.tournament.tournament_players:
                if match.player1._name == players._name:
                    players.score += match.score1
                if match.player2._name == players._name:
                    players.score += match.score2


class CreationPairMatch:
    def __init__(self, tournament, round_game):
        self.tournament = tournament
        self.round = round_game

    def __call__(self, *args, **kwargs):

        pairs_history = []
        for round_game in self.tournament.list_round:
            for match in round_game.matchs:
                pairs_history.append((match.player1, match.player2))

        remaining_players = self.tournament.get_remaining_players()

        while len(remaining_players) >= 2:
            player1 = remaining_players.pop(0)
            player2 = None
            for other_player in remaining_players:
                if (player1, other_player) not in pairs_history and (
                        other_player, player1) not in pairs_history:
                    player2 = other_player
                    remaining_players.remove(player2)
                    new_match = Match(player1, player2, date_save=datetime.now().isoformat())
                    self.round.add_match(new_match)
                    pairs_history.append((player1, player2))
                    break
            if player2 is None:
                player2 = remaining_players.pop(0)
                new_match = Match(player1, player2, date_save=datetime.now().isoformat())
                self.round.add_match(new_match)
                pairs_history.append((player1, player2))
