from views.menu_view import HomeMenuView  #, PlayerMenuView, ChoosePlayerMenuView
from models.player import Player
from models.menu import Menu


class ApplicationController:
    def __init__(self):
        self.controller = None

    def start(self):
        self.controller = HomeMenuController()
        while self.controller:
            self.controller = self.controller()

    def player(self):
        self.controller = PlayerMenuController()
        while self.controller:
            self.controller = self.controller()

    def chooseplayer(self):
        self.controller = MenulistePlayerController()
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
    def __init__(self):
        self.menu = Menu()
        self.view = HomeMenuView(self.menu)

    def __call__(self, *args, **kwargs):
        # 1.construire un menu
        self.menu.add("auto", "Ajouter joueur depuis la liste", MenulistePlayerController())
        self.menu.add("auto", "Ajouter joueu manuellement", MenuResultTournamentController())
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
    def __call__(self, *args, **kwargs):
        print("dans le controleur de LISTE DES JOUEURS")


class QuitController:
    def __call__(self, *args, **kwargs):
        print("dans le controleur de fin")


class MenulistePlayerController:
    def __init__(self):
        self.menu = Menu()
        self.view = HomeMenuView(self.menu)

    def __call__(self, *args, **kwargs):
        print("dans le controleur d'affichages de tous les joueurs")
        list_player = Player.from_tinydb_all("./all_players.json", "all_player", False)
        print(list_player)
        for player in list_player:
            print(player)
            self.menu.add("auto", f"{player}",Addplayer(player))
        user_choice = self.view.get_user_choice()
        return user_choice.handler

        # app = ApplicationController()
        # app.chooseplayer()
        # menu = Menu()


class Addplayer:
    def __init__(self,player=None):
        self.player = player

    def __call__(self, *args, **kwargs):
        print(self.player)
