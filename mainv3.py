from models.player import Player
from models.tournament import Tournament
from models.menu import MenuEntry, Menu
from models.round import Round
from models.match import Match
from views.player_view import PlayerView
from views.tournament_view import TournamentView
from views.menu_view import HomeMenuView
from views.round_view import RoundView
from views.match_view import MatchView
from controllers.player_controllers import PlayerController
from controllers.tournamenent_controllers import TournamentController
from controllers.menu_controllers import ApplicationController, HomeMenuController, MenuNewTournamentController
from controllers.round_controllers import RoundController
from controllers.match_controllers import MatchController

from datetime import date, timedelta
from tinydb import TinyDB, Query


player1 = Player("Dupont", "Adrien", date(1990, 5, 15), 50)
player2 = Player("Moline", "Séverine", date(1992, 2, 1), 500)
player3 = Player("Kagon", "Nino", date(1988, 11, 4), 350)
player4 = Player("Guyot", "Maxime", date(1998, 3, 27), 400)
player5 = Player("Dalco", "Lucien", date(1995, 8, 12), 500)
# player6 = Player("Vardie", "Jennifer", date(1995, 7, 21), 275)
# player7 = Player("Dupont", "Adrien", date(1990, 5, 15), 50)

# #*********************     TOURNOI     **************************
date_start = date(2023, 10, 14)
date_end = date_start + timedelta(4)
championnat = Tournament("championnat académique", "Cergy", "12fevrier", "13marss", 5)
controller_tournoi = TournamentController(championnat)

controller_tournoi.add_tournament_player_controller(player1)
controller_tournoi.add_tournament_player_controller(player2)
controller_tournoi.add_tournament_player_controller(player3)
controller_tournoi.add_tournament_player_controller(player4)
controller_tournoi.add_tournament_player_controller(player5)
# controller_tournoi.add_tournament_player_controller(player6)
print(f'list de joueuers:{championnat.tournament_players}')

controller_tournoi.display_tournament_info_controler()
controller_tournoi.display_player_tournament_controler()

championnat.save_player_tournament_to_json()
championnat.save_tournament_info_to_json()
print()
championnat.set_name("TOTO")
print(championnat)
championnat=Tournament.from_tinydb()
print(championnat)

championnat.actual_round=2
print(f'list de joueuers:{championnat.tournament_players}')

for tour in range(championnat.numbers_round-championnat.actual_round+1):

    print(f'************************Round numero {championnat.actual_round}***************\n')
    championnat.increment_actual_round()
    round = Round()

    if championnat.nombre__de_participant_pair():
        i = 1
        for personne in range(0, championnat.nombre_de_participants(), 2):  # creation de variable match123
            match_save = Match(championnat[personne][0], championnat[personne][1], championnat[personne + 1][0],
                               championnat[personne + 1][1])
            round.matchs.append(match_save)
    print(championnat.list_round)

    round.set_numero(tour + 1)

    print("Affichage match:")
    for item in round.matchs:  # premier match
        print(item)
    print()

    print("Affichage Gagnant:")
    for match in round.matchs:  # simulation joueur gagnant

        print(match)
        match.random_gagnant()
        print(match)
    print("Save round:")
    print(round.matchs)
    championnat.list_round.append(round.matchs)
    print(championnat.list_round)

print("***********************Fin tournoi***************")

print()

print(championnat[0])
print(Player.from_tinydb_all())

print(championnat.list_round)

# ################### exemple code recherche  ########################
# # db=TinyDB(r'C:\Users\Ghost\OneDrive\Documents\Openclassrooms\Projet_4\chess_tournaments\tournoi\players.json')
# # doc_id_to_find = 1
# # Record = Query()
# # result = db.get(doc_id=1)
# # name=result.get("name")
# # print(name)
# ####################################################################
