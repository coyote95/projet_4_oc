from models.player import Player
from models.tournament import Tournament
from models.menu import MenuEntry, Menu
from views.menu_view import HomeMenuView
from controllers.player_controllers import PlayerController
from controllers.Run import Run, RunCreationTournoi
import views

import sys


class ApplicationController:
    def __init__(self):
        self.controller = None

    def start(self):
        self.controller = HomeMenuController()
        while self.controller:
            self.controller = self.controller()

    def choixgagnantmatch(self, match):
        self.match = match
        self.controller = MenuChoixgagnantPlayerController(self.match)
        while self.controller:
            self.controller = self.controller()

    def ChoixJouerleRound(self, round):
        self.round = round
        self.controller = MenuChoixJouerleRound(self.round)
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
        self.menu.add("auto", "Reprendre tournoi", MenuReprendreTournamentController())
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


class MenuReprendreTournamentController:
    def __init__(self):
        self.menu = Menu()
        self.view = HomeMenuView(self.menu)

    def __call__(self, *args, **kwargs):
        print("dans le controleur de REPRENDRE UN TOURNOI")

        list_tournaments = Tournament.from_tinydb_all("./data/tournaments.json")
        print(f'nombre de tournoi:{len(list_tournaments)}')

        for tournament in list_tournaments:
            print(f"round total:{tournament.get_numbers_round()}")
            print(f"round actual:{tournament.get_actual_round()}")
            print(tournament.list_round)
            if tournament.get_numbers_round() == tournament.get_actual_round():
                print("tournoi terminé")
            else:
                self.menu.add("auto", f"Nom: {tournament.get_name()} Place: {tournament.get_place()}",
                              Run(tournament))

        self.menu.add("r", "Retour", HomeMenuController())
        self.menu.add("q", "Quitter", QuitController())
        user_choice = self.view.get_user_choice()
        print(user_choice)
        return user_choice.handler


class MenuPrincipalListPlayersController:

    def __init__(self):
        self.menu = Menu()
        self.view = HomeMenuView(self.menu)

    def __call__(self, *args, **kwargs):
        list_player = Player.from_tinydb_all("./data/all_players.json", False)
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
        print("Fin du programme")
        sys.exit()


class MenulistePlayerController:
    def __init__(self, tournament):
        self.menu = Menu()
        self.view = HomeMenuView(self.menu)
        self.tournament = tournament

    def __call__(self, *args, **kwargs):
        print("dans le controleur d'affichages de tous les joueurs")
        list_player = Player.from_tinydb_all("./data/all_players.json", False)
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
        print(f'nombre de tournoi:{len(list_tournaments)}')

        for tournament in list_tournaments:
            self.menu.add("auto", f"Nom: {tournament.get_name()} Place: {tournament.get_place()}",
                          views.tournament_view.TournamentView(tournament))

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


class MenuChoixgagnantPlayerController:
    def __init__(self, match):
        self.menu = Menu()
        self.view = HomeMenuView(self.menu)
        self.match = match

    def __call__(self, *args, **kwargs):
        print("Le gagant est")
        self.menu.add("auto", f"{self.match.player1}", lambda: self.match.winner(self.match.player1))
        self.menu.add("auto", f"{self.match.player2}", lambda: self.match.winner(self.match.player2))
        self.menu.add("auto", f"match null", lambda: self.match.winner("execo"))
        user_choice = self.view.get_user_choice()
        return user_choice.handler


class MenuChoixJouerleRound:
    def __init__(self, round):
        self.menu = Menu()
        self.view = HomeMenuView(self.menu)
        self.round = round

    def __call__(self, *args, **kwargs):
        print(f"Voulez vous jouer le round {self.round.get_numero_round()} ?")
        self.menu.add("auto", f"OUI", lambda: None)
        self.menu.add("auto", f"NON", QuitController())
        user_choice = self.view.get_user_choice()
        return user_choice.handler
