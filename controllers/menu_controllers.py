from views.menu_view import HomeMenuView
from models.menu import Menu


class ApplicationController:
    def __init__(self):
        self.controller = None

    def start(self):
        self.controller = HomeMenuController()
        while self.controller:
            self.controller = self.controller()


class HomeMenuController:
    def __init__(self):
        self.menu = Menu()
        self.view = HomeMenuView(self.menu)

    def __call__(self, *args, **kwargs):
        # 1.construire un menu
        self.menu.add("auto", " Création nouveau tournoi", MenuNewTournamentController())
        self.menu.add("auto", "Résultat ancien tournoi", MenuResultTournamentController())
        self.menu.add("auto", "liste des joueurs", MenuListPlayersController())
        self.menu.add("q", "quitter", QuitController())
        # 2. Demander à la vue d'afficher le menu et de collecter la réponse de l'utilisateur
        user_choice = self.view.get_user_choice()
        # 3. retourner le controller associé au choix de l'utilisateur au controller principal
        return user_choice.handler


class MenuNewTournamentController:
    def __call__(self, *args, **kwargs):
        print("Entrer le nom du championnat")


class MenuResultTournamentController:
    def __call__(self, *args, **kwargs):
        print("dans le controleur de RESULTAT ANCIEN TOURNOI")


class MenuListPlayersController:
    def __call__(self, *args, **kwargs):
        print("dans le controleur de LISTE DES JOUEURS")


class QuitController:
    def __call__(self, *args, **kwargs):
        print("dans le controleur de fin")
