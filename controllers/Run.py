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
        controller_tournoi.save_player_tournament_to_json_controller(filename=controller_tournoi.get_name_controller())
        controller_tournoi.save_tournament_info_to_json_controller(filename=controller_tournoi.get_name_controller())
        controller_tournoi.display_player_tournament_controler()
        run_instance = Run(self.tournament)
        run_instance()


class Run:
    def __init__(self, tournament):
        self.tournament = tournament

    def __call__(self, *args, **kwargs):

        print(f'list de joueurs participants au tournoi:{self.tournament.tournament_players}')

        for tour in range(self.tournament.numbers_round - self.tournament.actual_round + 1):

            for personne in range(0, len(self.tournament)):
                self.tournament.tournament_players = sorted(self.tournament.tournament_players,
                                                            key=lambda player: player.score,
                                                            reverse=True)

            print(f'************************Round numero {self.tournament.actual_round}***************\n')
            self.tournament.increment_actual_round()
            round_tournament = Round()
            round_tournament.set_numero(tour + 1)
            round_tournament.commence = datetime.now().isoformat()

            if self.tournament.nombre__de_participant_pair():
                for personne in range(0, self.tournament.nombre_de_participants(), 2):  # creation de variable match123
                    match_save = Match(self.tournament[personne], self.tournament[personne + 1], )
                    round_tournament.matchs.append(match_save)
            else:  # on retire le joueur pour creer match
                for personne in range(0, self.tournament.nombre_de_participants() - 1,
                                      2):  # creation de variable match123
                    match_save = Match(self.tournament[personne], self.tournament[personne + 1], )
                    round_tournament.matchs.append(match_save)

            print("Affichage match:")
            for item in round_tournament.matchs:  # premier match
                print(item)
            print()

            print("Affichage Gagnant:")

            for match in round_tournament.matchs:  # simulation joueur gagnant
                match.random_gagnant()

            self.tournament.list_round.append(round_tournament)

            if self.tournament.nombre__de_participant_pair():
                i = 0
                j = 0
                for personne in self.tournament.tournament_players:  # mise a jour score total joueur
                    if j % 2 == 0:
                        personne.score += round_tournament.matchs[i].score1

                    else:
                        personne.score += round_tournament.matchs[i].score2
                        i += 1
                    j += 1
            else:
                i = 0
                j = 0
                for personne in self.tournament.tournament_players[:-1]:  # mise a jour score total joueur
                    if j % 2 == 0:
                        personne.score += round_tournament.matchs[i].score1

                    else:
                        personne.score += round_tournament.matchs[i].score2
                        i += 1
                    j += 1

            for personne in range(0, len(self.tournament)):
                print(self.tournament[personne])
                print(self.tournament[personne].score)

            print(self.tournament.tournament_players)

            self.tournament.save_player_tournament_to_json()
            self.tournament.save_round_tournament_to_json()

            round_tournament.termine = datetime.now().isoformat()

        print("***********************Fin tournoi***************")

        print()

        for i in range(len(self.tournament.tournament_players)):
            print(self.tournament[i])

        print(Player.from_tinydb_all())

        print(self.tournament.list_round)
        print()

        for j in range(len(self.tournament.list_round)):
            print(self.tournament.list_round[j])

        print(self.tournament)
