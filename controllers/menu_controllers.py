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
        self.menu.add("auto", "classement", ClassementMenuController())
        self.menu.add("auto", "commencer_un_tournois", NewTournamentController())
        self.menu.add("q", "quitter", QuitController())
        # 2. Demander à la vue d'afficher le menu et de collecter la réponse de l'utilisateur
        user_choice = self.view.get_user_choice()
        # 3. retourner le controller associé au choix de l'utilisateur au controller principal
        return user_choice.handler


class ClassementMenuController:
    def __call__(self, *args, **kwargs):
        print("dans le controleur de classement ")


class NewTournamentController:
    def __init__(self):
        pass


class QuitController:
    pass
