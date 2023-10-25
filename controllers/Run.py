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
       # controller_tournoi.save_player_tournament_to_json_controller()
        controller_tournoi.save_tournament_info_to_json_controller()
        controller_tournoi.display_player_tournament_controler()
        run_instance = Run(self.tournament)
        run_instance()


class Run:
    def __init__(self, tournament):
        self.tournament = tournament

    def __call__(self, *args, **kwargs):
        controller_tournoi = TournamentController(self.tournament)

        for tour in range(self.tournament.get_numbers_round() - self.tournament.get_actual_round() + 1):
            controller_tournoi.sort_players_by_score_controller()
            controller_tournoi.display_actual_numero_round_controller()
            controller_tournoi.increment_actual_round_controller()

            round_tournament = Round()
            controller_round = RoundController(round_tournament)
            controller_round.set_numero_controller(tour + 1)
            controller_round.set_commence_controller(datetime.now().isoformat())

            if controller_tournoi.nombre_de_participant_pair_controller():
                for personne in range(0, controller_tournoi.nombre_de_participants_controller(), 2):
                    new_match = Match(controller_tournoi[personne], controller_tournoi[personne + 1])
                    controller_round.add_match_controller(new_match)
            else:  # on retire le joueur pour creer match
                for personne in range(0, controller_tournoi.nombre_de_participants_controller() - 1, 2):
                    new_match = Match(controller_tournoi[personne], controller_tournoi[personne + 1])
                    controller_round.add_match_controller(new_match)

            controller_round.display_match_controller()

            print("Affichage Gagnant:")
            for match in controller_round.get_match_controller():
                controller_match = MatchController(match)
                controller_match.random_gagnant_controller()

            controller_tournoi.add_list_tournament_round_controller(round_tournament)

            score_instance = UpdateScoreRun(self.tournament, round_tournament)
            score_instance()

            controller_tournoi.score_player_tournament_controller()

          #  controller_tournoi.save_player_tournament_to_json_controller(
          #      filename=controller_tournoi.get_name_controller())
            controller_tournoi.save_round_tournament_to_json_controller(
                filename=controller_tournoi.get_name_controller())

            controller_round.set_termine_controller(datetime.now().isoformat())

        print(f"***********************Fin tournoi***************\n")

        for i in range(len(self.tournament.tournament_players)):
            print(self.tournament[i])

        for j in range(len(self.tournament.list_round)):
            print(self.tournament.list_round[j])




class UpdateScoreRun:
    def __init__(self, tournament, round):
        self.tournament = tournament
        self.round = round

    def __call__(self, *args, **kwargs):

        if self.tournament.nombre_de_participant_pair():
            i = 0
            j = 0
            for player in self.tournament.tournament_players:  # mise a jour score total joueur
                if j % 2 == 0:
                    player.score += self.round.matchs[i].score1

                else:
                    player.score += self.round.matchs[i].score2
                    i += 1
                j += 1
        else:
            i = 0
            j = 0
            for player in self.tournament.tournament_players[:-1]:  # mise a jour score total joueur
                if j % 2 == 0:
                    player.score += self.round.matchs[i].score1

                else:
                    player.score += self.round.matchs[i].score2
                    i += 1
                j += 1
