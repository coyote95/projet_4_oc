from models.player import Player
from models.tournament import Tournament
from models.menu import Menu
from views.menu_view import HomeMenuView
from views.tournament_view import TournamentView
from controllers.player_controllers import PlayerController
from controllers.Run import Run, RunCreationTournoi
import sys


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
        self.controller = MenuChoixgagnantPlayerController(self.match)
        while self.controller:
            self.controller = self.controller()

    def choixjouerleround(self, game_round):
        self.round = game_round
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
        self.view.display_message_accueil()
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


class MenuReprendreTournamentController:
    def __init__(self):
        self.menu = Menu()
        self.view = HomeMenuView(self.menu)

    def __call__(self, *args, **kwargs):
        self.view.display_message_reprendre_tournoi()

        list_tournaments = Tournament.from_tinydb_all("./data/tournaments.json")

        for tournament in list_tournaments:
            if not tournament.get_numbers_round() == tournament.get_actual_round():
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
        self.view.display_message_list_players()
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
    def __init__(self):
        self.menu = Menu()
        self.view = HomeMenuView(self.menu)

    def __call__(self, *args, **kwargs):
        self.view.display_message_end_programme()
        sys.exit()


class MenulistePlayerController:
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


class MenulisteTournamentController:
    def __init__(self):
        self.menu = Menu()
        self.view = HomeMenuView(self.menu)

    def __call__(self, *args, **kwargs):
        self.view.display_message_liste_tournoi()
        list_tournaments = Tournament.from_tinydb_all("./data/tournaments.json")
        for tournament in list_tournaments:
            self.menu.add("auto", f"Nom: {tournament.get_name()} Place: {tournament.get_place()}",
                          MenuInfoTournamentReturnController(tournament))
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
        PlayerController(player).save_player_controller(filename="./data/all_players.json",
                                                        score=False)
        self.tournament.add_tournament_player(player)


class MenuChoixgagnantPlayerController:
    def __init__(self, match):
        self.menu = Menu()
        self.view = HomeMenuView(self.menu)
        self.match = match

    def __call__(self, *args, **kwargs):
        self.view.display_message_gagnant()
        self.menu.add("auto", f"{self.match.player1}", lambda: self.match.winner(self.match.player1))
        self.menu.add("auto", f"{self.match.player2}", lambda: self.match.winner(self.match.player2))
        self.menu.add("auto", f"match null", lambda: self.match.winner("execo"))
        user_choice = self.view.get_user_choice()
        return user_choice.handler


class MenuChoixJouerleRound:
    def __init__(self, game_round):
        self.menu = Menu()
        self.view = HomeMenuView(self.menu)
        self.round = game_round

    def __call__(self, *args, **kwargs):
        self.view.display_message_continue(self.round.get_numero_round())
        self.menu.add("auto", f"OUI", lambda: None)
        self.menu.add("auto", f"NON", HomeMenuController())
        user_choice = self.view.get_user_choice()
        return user_choice.handler
