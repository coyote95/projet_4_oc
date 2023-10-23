from views.menu_view import HomeMenuView  # , PlayerMenuView, ChoosePlayerMenuView
from models.player import Player
from models.tournament import Tournament
from controllers.tournamenent_controllers import TournamentController
from controllers.player_controllers import PlayerController
from models.menu import Menu
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
        self.menu.add("auto", "Création nouveau tournoi", MenuNewTournamentController())
        self.menu.add("auto", "Résultat ancien tournoi", MenuResultTournamentController())
        self.menu.add("auto", "Liste des joueurs", MenuListPlayersController())
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
        self.menu.add("auto", "Ajouter joueu manuellement", ManuelPlayer(self.tournament))
        user_choice = self.view.get_user_choice()
        return user_choice.handler


class MenuNewTournamentController:
    def __call__(self, *args, **kwargs):
        print()
        print("Appleler creation d'un tournoi ")


class MenuResultTournamentController:
    def __call__(self, *args, **kwargs):
        print("dans le controleur de RESULTAT ANCIEN TOURNOI")


class MenuListPlayersController:

    def __init__(self):
        self.menu = Menu()
        self.view = HomeMenuView(self.menu)

    def __call__(self, *args, **kwargs):
        print("dans le controleur d'affichages de tous les joueurs")
        list_player = Player.from_tinydb_all("./all_players.json", "all_player", False)
        i=1
        for player in list_player:
            print(f"{i}: {player}")
            i+=1

        self.menu.add("r", "Retour", HomeMenuController())
        self.menu.add("q", "Quitter", QuitController())
        user_choice = self.view.get_user_choice()
        print(user_choice)
        return user_choice.handler
        return None


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
        list_player = Player.from_tinydb_all("./all_players.json", "all_player", False)
        print(list_player)
        for player in list_player:
            self.menu.add("auto", f"{player}", Addplayer(player, self.tournament))
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
        self.tournament.add_tournament_player(player)
