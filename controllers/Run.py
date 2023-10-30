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

        for tour in range(self.tournament.get_numbers_round() - self.tournament.get_actual_round()):
            controller_tournoi.sort_players_by_score_controller()
            controller_tournoi.display_player_tournament_controler()

            controller_tournoi.increment_actual_round_controller()
            controller_tournoi.display_actual_numero_round_controller()

            round_tournament = Round()
            # round_tournament.matchs.clear()  # Pourquoi doit clear
            controller_round = RoundController(round_tournament)
            controller_round.set_numero_controller(controller_tournoi.get_actual_round_controller())
            controller_round.set_commence_controller(datetime.now().isoformat())

            #           pair history

            pairs_history = []

            for round in self.tournament.list_round:
                for match in round.matchs:
                    pairs_history.append((match.player1, match.player2))

            print(pairs_history)

            #                    code tournoi
            print(controller_tournoi.nombre_de_participants_controller())
            #if controller_tournoi.nombre_de_participant_pair_controller():
                # Liste des joueurs restants
            remaining_players = self.tournament.get_remaining_players()
            print(f"remaining player:{remaining_players}")

            while len(remaining_players) >= 2:
                print("je refais la boucle")
                player1 = remaining_players.pop(0)

                print("player1:")
                print(player1)

                player2 = None
                for other_player in remaining_players:

                    if (player1, other_player) not in pairs_history and (
                    other_player, player1) not in pairs_history:
                        player2 = other_player
                        remaining_players.remove(player2)
                        print("player2:")
                        print(player2)

                        new_match = Match(player1, player2,date_save=datetime.now().isoformat())
                        controller_round.add_match_controller(new_match)
                        pairs_history.append((player1, player2))
                        break
                if player2 is None:
                    player2 = remaining_players.pop(0)
                    new_match = Match(player1, player2,date_save=datetime.now().isoformat())
                    controller_round.add_match_controller(new_match)
                    pairs_history.append((player1, player2))

            controller_round.display_match_controller()

            print("Affichage Gagnant:")
            for match in controller_round.get_match_controller():
                controller_match = MatchController(match)
                controller_match.random_gagnant_controller()
                controller_match.save_match_to_json_controller()

            controller_tournoi.add_list_tournament_round_controller(round_tournament)

            score_instance = UpdateScoreRun(self.tournament, round_tournament)
            score_instance()

            controller_tournoi.score_player_tournament_controller()

            controller_tournoi.save_player_tournament_to_json_controller()
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
        for round in self.tournament.list_round:
            for match in round.matchs:
                print(match)


class UpdateScoreRun:
    def __init__(self, tournament, round):
        self.tournament = tournament
        self.round = round

    def __call__(self, *args, **kwargs):

        for match in self.round.matchs:
            for players in self.tournament.tournament_players:
                if match.player1._name == players._name:
                    players.score += match.score1
                if match.player2._name == players._name:
                    players.score += match.score2

        # if self.tournament.nombre_de_participant_pair():
        #     i = 0
        #     j = 0
        #     for player in self.tournament.tournament_players:  # mise a jour score total joueur
        #         if j % 2 == 0:
        #             player.score += self.round.matchs[i].score1
        #
        #         else:
        #             player.score += self.round.matchs[i].score2
        #             i += 1
        #         j += 1
        # else:
        #     i = 0
        #     j = 0
        #     for player in self.tournament.tournament_players[:-1]:  # mise a jour score total joueur
        #         if j % 2 == 0:
        #             player.score += self.round.matchs[i].score1
        #
        #         else:
        #             player.score += self.round.matchs[i].score2
        #             i += 1
        #         j += 1
