import sys

import controllers.player_controllers
from controllers.match_controllers import MatchController
from controllers.player_controllers import PlayerController
from controllers.Run import Run, RunCreationTournoi
from models.menu import Menu
from models.player import Player
from models.tournament import Tournament
from views.menu_view import HomeMenuView
from views.tournament_view import TournamentView


class ApplicationController:
    def __init__(self):
        self.controller = None
        self.match = None
        self.round = None
        self.tournament = None

    def start(self):
        self.controller = HomeMenuController()
        while self.controller:
            self.controller = self.controller()

    def choixgagnantmatch(self, match):
        self.match = match
        self.controller = MenuChoiceWinnerPlayerController(self.match)
        while self.controller:
            self.controller = self.controller()

    def choixjouerleround(self, game_round):
        self.round = game_round
        self.controller = MenuChoicePlayRound(self.round)
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
        self.view.display_message_accueil()
        self.menu.add("auto", "Création nouveau tournoi", RunCreationTournoi())
        self.menu.add("auto", "Reprendre tournoi", MenuReprendreTournamentController())
        self.menu.add("auto", "Résultat ancien tournoi", MenuListTournamentController())
        self.menu.add("auto", "Ajouter joueurs ", MenuAddPlayer)
        self.menu.add("auto", "Liste des joueurs", MenuPrincipalListPlayersController())
        self.menu.add("q", "Quitter", QuitController())
        user_choice = self.view.get_user_choice()
        return user_choice.handler


class PlayerMenuController:
    def __init__(self, tournament):
        self.menu = Menu()
        self.view = HomeMenuView(self.menu)
        self.tournament = tournament

    def __call__(self, *args, **kwargs):
        self.menu.add(
            "auto",
            "Ajouter joueur depuis la liste",
            MenuChoiceListAddPlayerController(self.tournament),
        )
        self.menu.add(
            "auto", "Ajouter joueur manuellement", ManuelPlayer(self.tournament)
        )
        user_choice = self.view.get_user_choice()
        return user_choice.handler


class MenuReprendreTournamentController:
    def __init__(self):
        self.menu = Menu()
        self.view = HomeMenuView(self.menu)

    def __call__(self, *args, **kwargs):
        self.view.display_message_reprendre_tournoi()

        list_tournaments = Tournament.from_tinydb_all("./data/tournaments" ".json")
        # Verify if tournament is finish else display tournament
        for tournament in list_tournaments:
            if not (tournament.get_numbers_round() == tournament.get_actual_round()):
                self.menu.add(
                    "auto",
                    f"Nom: {tournament.get_name()}" f" Place: {tournament.get_place()}",
                    Run(tournament),
                )

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
        self.view.display_message_list_players()
        list_player = Player.from_tinydb_all("./data/all_players.json", False)

        sorted_players = sorted(list_player, key=lambda player_class: player_class.name)
        for player in sorted_players:
            player_controller = controllers.player_controllers.PlayerController(player)
            player_controller.display_player_controller()

        self.menu.add("r", "Retour", HomeMenuController())
        self.menu.add("q", "Quitter", QuitController())
        user_choice = self.view.get_user_choice()
        print(user_choice)
        return user_choice.handler


class QuitController:
    def __init__(self):
        self.menu = Menu()
        self.view = HomeMenuView(self.menu)

    def __call__(self, *args, **kwargs):
        self.view.display_message_end_programme()
        sys.exit()


class MenuChoiceListAddPlayerController:
    """
    Menu for choice add player in tournaments.
    """

    def __init__(self, tournament):
        self.menu = Menu()
        self.view = HomeMenuView(self.menu)
        self.tournament = tournament

    def __call__(self, *args, **kwargs):
        self.view.display_message_list_players()
        list_player = Player.from_tinydb_all("./data/all_players.json", False)
        for player in list_player:
            self.menu.add("auto", f"{player}", Addplayer(player, self.tournament))
        user_choice = self.view.get_user_choice()
        print(user_choice)
        return user_choice.handler


class MenuListTournamentController:
    def __init__(self):
        self.menu = Menu()
        self.view = HomeMenuView(self.menu)

    def __call__(self, *args, **kwargs):
        self.view.display_message_liste_tournoi()
        list_tournaments = Tournament.from_tinydb_all("./data/tournaments.json")
        for tournament in list_tournaments:
            self.menu.add(
                "auto",
                f"Nom: {tournament.get_name()}" f" Place: {tournament.get_place()}",
                MenuInfoTournamentReturnController(tournament),
            )
        self.menu.add("r", "Retour", HomeMenuController())
        self.menu.add("q", "Quitter", QuitController())
        user_choice = self.view.get_user_choice()
        print(user_choice)
        return user_choice.handler


class MenuInfoTournamentReturnController:
    def __init__(self, tournament):
        self.menu = Menu()
        self.view = HomeMenuView(self.menu)
        self.tournament = tournament

    def __call__(self, *args, **kwargs):
        instance = TournamentView(self.tournament)
        instance()
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
        player = Player(None, None, None, None)
        PlayerController(player).creation_player()
        PlayerController(player).save_player_controller(
            filename="./data/all_players.json", score=False
        )
        self.tournament.add_tournament_player(player)


class MenuAddPlayer:
    def __init__(self, tournament=None):
        self.menu = Menu()
        self.view = HomeMenuView(self.menu)

    def __call__(self, *args, **kwargs):
        player = Player(None, None, None, None)
        PlayerController(player).creation_player()
        PlayerController(player).save_player_controller(
            filename="./data/all_players.json", score=False
        )
        self.menu.add("r", "Retour", HomeMenuController())
        self.menu.add("q", "Quitter", QuitController())
        user_choice = self.view.get_user_choice()
        print(user_choice)
        return user_choice.handler


class MenuChoiceWinnerPlayerController:
    def __init__(self, match):
        self.menu = Menu()
        self.view = HomeMenuView(self.menu)
        self.match = match

    def __call__(self, *args, **kwargs):
        match_controller = MatchController(self.match)
        self.view.display_message_gagnant()
        self.menu.add(
            "auto",
            f"Joueur1: {self.match.player1.name}" f" {self.match.player1.surname}",
            lambda: match_controller.winner_controller(self.match.player1),
        )
        self.menu.add(
            "auto",
            f"Joueur2: {self.match.player2.name}" f" {self.match.player2.surname}",
            lambda: match_controller.winner_controller(self.match.player2),
        )
        self.menu.add(
            "auto", "match null", lambda: match_controller.winner_controller("execo")
        )
        user_choice = self.view.get_user_choice()
        return user_choice.handler


class MenuChoicePlayRound:
    """
    Menu Choice continu to play round or not
    """

    def __init__(self, game_round):
        self.menu = Menu()
        self.view = HomeMenuView(self.menu)
        self.round = game_round

    def __call__(self, *args, **kwargs):
        self.view.display_message_continue(self.round.get_numero_round())
        self.menu.add("auto", "OUI", lambda: None)
        self.menu.add("auto", "NON", HomeMenuController())
        user_choice = self.view.get_user_choice()
        return user_choice.handler
