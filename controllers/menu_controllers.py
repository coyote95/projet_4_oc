from models.player import Player
from models.tournament import Tournament
from models.menu import MenuEntry, Menu
from models.round import Round
from models.match import Match
from views.player_view import PlayerView
# from views.tournament_view import TournamentView
from views.menu_view import HomeMenuView
from views.round_view import RoundView
from views.match_view import MatchView
from controllers.player_controllers import PlayerController
from controllers.tournamenent_controllers import TournamentController
from controllers.round_controllers import RoundController
from controllers.match_controllers import MatchController
from controllers.Run import Run, RunCreationTournoi

from datetime import date, timedelta, datetime
from tinydb import TinyDB, Query
import sys


class ApplicationController:
    def __init__(self):
        self.controller = None

    def start(self):
        self.controller = HomeMenuController()
        while self.controller:
            self.controller = self.controller()

    def player(self, tournament):
        self.tournament = tournament
        self.controller = PlayerMenuController(self.tournament)

        while self.controller:
            self.controller = self.controller()


class HomeMenuController:
    def __init__(self):
        self.menu = Menu()
        self.view = HomeMenuView(self.menu)

    def __call__(self, *args, **kwargs):
        # 1.construire un menu
        self.menu.add("auto", "Création nouveau tournoi", RunCreationTournoi())
        self.menu.add("auto", "Reprendre tournoi", MenuResultTournamentController())
        self.menu.add("auto", "Résultat ancien tournoi", MenulisteTournamentController())
        self.menu.add("auto", "Liste des joueurs", MenuPrincipalListPlayersController())
        self.menu.add("q", "Quitter", QuitController())
        # 2. Demander à la vue d'afficher le menu et de collecter la réponse de l'utilisateur
        user_choice = self.view.get_user_choice()
        # 3. retourner le controller associé au choix de l'utilisateur au controller principal
        return user_choice.handler


class PlayerMenuController:
    def __init__(self, tournament):
        self.menu = Menu()
        self.view = HomeMenuView(self.menu)
        self.tournament = tournament

    def __call__(self, *args, **kwargs):
        # 1.construire un menu
        self.menu.add("auto", "Ajouter joueur depuis la liste", MenulistePlayerController(self.tournament))
        self.menu.add("auto", "Ajouter joueur manuellement", ManuelPlayer(self.tournament))
        user_choice = self.view.get_user_choice()
        return user_choice.handler


class MenuNewTournamentController:
    def __call__(self, *args, **kwargs):
        print()
        print("Appleler creation d'un tournoi ")


class MenuResultTournamentController:
    def __call__(self, *args, **kwargs):
        print("dans le controleur de RESULTAT ANCIEN TOURNOI")


class MenuPrincipalListPlayersController:

    def __init__(self):
        self.menu = Menu()
        self.view = HomeMenuView(self.menu)

    def __call__(self, *args, **kwargs):
        print("dans le controleur d'affichages de tous les joueurs")
        list_player = Player.from_tinydb_all("./data/all_players.json", "all_players", False)
        i = 1
        for player in list_player:
            print(f"{i}: {player}")
            i += 1

        self.menu.add("r", "Retour", HomeMenuController())
        self.menu.add("q", "Quitter", QuitController())
        user_choice = self.view.get_user_choice()
        print(user_choice)
        return user_choice.handler



class QuitController:
    def __call__(self, *args, **kwargs):
        print("dans le controleur de fin")
        sys.exit()


class MenulistePlayerController:
    def __init__(self, tournament):
        self.menu = Menu()
        self.view = HomeMenuView(self.menu)
        self.tournament = tournament

    def __call__(self, *args, **kwargs):
        print("dans le controleur d'affichages de tous les joueurs")
        list_player = Player.from_tinydb_all("./data/all_players.json",  False)
        print(list_player)
        for player in list_player:
            self.menu.add("auto", f"{player}", Addplayer(player, self.tournament))
        user_choice = self.view.get_user_choice()
        print(user_choice)
        return user_choice.handler


class MenulisteTournamentController:
    def __init__(self):
        self.menu = Menu()
        self.view = HomeMenuView(self.menu)

    def __call__(self, *args, **kwargs):
        print("dans le controleur d'affichages de tous les tournois")
        list_tournaments = Tournament.from_tinydb_all("./data/tournaments.json")
        i = 1
        for tournament in list_tournaments:
            print(f"{i}: Nom: {tournament.get_name()} Place: {tournament.get_place()}")
            i += 1

        self.menu.add("r", "Retour", HomeMenuController())
        self.menu.add("q", "Quitter", QuitController())
        user_choice = self.view.get_user_choice()
        print(user_choice)
        return user_choice.handler


class Addplayer:
    def __init__(self, player=None, tournament=None):
        self.player = player
        self.tournament = tournament

    def __call__(self, *args, **kwargs):
        print("Dans le controller ADDPLAYER")
        self.tournament.add_tournament_player(self.player)


class ManuelPlayer:
    def __init__(self, tournament=None):
        self.tournament = tournament

    def __call__(self, *args, **kwargs):
        print("Dans le controller Manuel")
        player = Player(None, None, None, None)
        PlayerController(player).creation_player()
        PlayerController(player).save_player_controller(filename="./data/all_players.json", table_name="all_players",
                                                        score=False)
        self.tournament.add_tournament_player(player)
