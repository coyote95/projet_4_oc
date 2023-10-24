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
        self.menu.add("auto", "Création nouveau tournoi", RunCreationTournoi())
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
        i = 1
        for player in list_player:
            print(f"{i}: {player}")
            i += 1

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


class RunCreationTournoi:
    def __init__(self):
        self.tournament = Tournament(None, None, None, None)

    def __call__(self, *args, **kwargs):
        controller_tournoi = TournamentController(self.tournament)
        controller_tournoi.creation_tournoi()
        print(self.tournament)

        print("Nombre de joueurs au tournoi:")

        while True:
            try:
                nombre_participant = input(">>")
                entier = int(nombre_participant)
                break
            except ValueError:
                print("L'entrée n'est pas un entier.")

        for tentative in range(0, int(nombre_participant)):
            print(f"Player {tentative + 1}")
            newplayer = Player(None, None, None, None)
            app = ApplicationController()
            app.player(self.tournament)
            menu = Menu()

        print(self.tournament.tournament_players)
        controller_tournoi.display_player_tournament_controler()
        Run()


class Run():
    def __init__(self,tournament):
        self.tournament=tournament

    def __call__(self, *args, **kwargs):

        print(f'list de joueurs participants au tournoi:{self.tournament.tournament_players}')

        for tour in range(self.tournament.numbers_round - self.tournament.actual_round + 1):

            for personne in range(0, len(self.tournament)):
                self.tournament.tournament_players = sorted(self.tournament.tournament_players, key=lambda player: player.score,
                                                        reverse=True)

            print(f'************************Round numero {self.tournament.actual_round}***************\n')
            championnat.increment_actual_round()
            round_tournament = Round()
            round_tournament.set_numero(tour + 1)
            round_tournament.commence= datetime.now().isoformat()



            if championnat.nombre__de_participant_pair():
                for personne in range(0, championnat.nombre_de_participants(), 2):  # creation de variable match123
                    match_save = Match(championnat[personne], championnat[personne + 1], )
                    round_tournament.matchs.append(match_save)
            else:  # on retire le joueur pour creer match
                for personne in range(0, championnat.nombre_de_participants() - 1, 2):  # creation de variable match123
                    match_save = Match(championnat[personne], championnat[personne + 1], )
                    round_tournament.matchs.append(match_save)



            print("Affichage match:")
            for item in round_tournament.matchs:  # premier match
                print(item)
            print()

            print("Affichage Gagnant:")

            for match in round_tournament.matchs:  # simulation joueur gagnant
                match.random_gagnant()

            championnat.list_round.append(round_tournament)

            if championnat.nombre__de_participant_pair():
                i = 0
                j = 0
                for personne in championnat.tournament_players:  # mise a jour score total joueur
                    if j % 2 == 0:
                        personne.score += round_tournament.matchs[i].score1

                    else:
                        personne.score += round_tournament.matchs[i].score2
                        i += 1
                    j += 1
            else:
                i = 0
                j = 0
                for personne in championnat.tournament_players[ :-1]:  # mise a jour score total joueur
                    if j % 2 == 0:
                        personne.score += round_tournament.matchs[i].score1

                    else:
                        personne.score += round_tournament.matchs[i].score2
                        i += 1
                    j += 1

            for personne in range(0, len(championnat)):
                print(championnat[personne])
                print(championnat[personne].score)

            print(championnat.tournament_players)

            championnat.save_player_tournament_to_json()
            championnat.save_round_tournament_to_json()

            round_tournament.termine= datetime.now().isoformat()

        print("***********************Fin tournoi***************")

        print()


        for i in range(len(championnat.tournament_players)):
            print(championnat[i])

        print(Player.from_tinydb_all())

        print(championnat.list_round)
        print()

        for j in range(len(championnat.list_round)):
            print(championnat.list_round[j])

