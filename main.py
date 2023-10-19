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
#
# ###########   Menu    ********************************
# app = ApplicationController()
# app.start()
# menu = Menu()
#
# #### ***********************   TOURNOI    ********************************
# newtournament = Tournament(None, None, None, None)
#
# controller_tournoi = TournamentController(newtournament)
# controller_tournoi.creation_tournoi()
# print(newtournament)
#
# print("Nombre de joueurs au tournoi:")
#
# while True:
#     try:
#         nombre_participant = input(">>")
#         entier = int(nombre_participant)
#         break
#     except ValueError:
#         print("L'entrée n'est pas un entier.")
#
#
# for tentative in range(0, int(nombre_participant)):
#     print(f"Player {tentative + 1}")
#     newplayer = Player(None, None, None, None)
#     PlayerController(newplayer).creation_player()
#     print(f"Resume:{newplayer}\n")
#     controller_tournoi.add_tournament_player_controller(newplayer)
#
# controller_tournoi.display_player_tournament_controler()
#
#         ## ************************  player  ******************************
#
player1 = Player("Dupont", "Adrien", date(1990, 5, 15), 50)
player2 = Player("Moline", "Séverine", date(1992, 2, 1), 500)
player3 = Player("Kagon", "Nino", date(1988, 11, 4), 350)
player4 = Player("Guyot", "Maxime", date(1998, 3, 27), 400)
player5 = Player("Dalco", "Lucien", date(1995, 8, 12), 500)
player6 = Player("Vardie", "Jennifer", date(1995, 7, 21), 275)
player7 = Player("Dupont", "Adrien", date(1990, 5, 15), 50)
# #
# db = TinyDB("Players.json")
# db.truncate()
#
# PlayerController(player1).save_player_controller()
# PlayerController(player2).save_player_controller()
# PlayerController(player3).save_player_controller()
# PlayerController(player4).save_player_controller()
# PlayerController(player5).save_player_controller()
# PlayerController(player1).display_player_controller()


# ####***********************************   SIMULATION  ***********************************************

# #*********************     TOURNOI     **************************
date_start = date(2023, 10, 14)
date_end = date_start + timedelta(4)
championnat = Tournament("championnat académique", "Cergy", date_start, date_end, 6)
controller_tournoi = TournamentController(championnat)

controller_tournoi.add_tournament_player_controller(player1)
controller_tournoi.add_tournament_player_controller(player2)
controller_tournoi.add_tournament_player_controller(player3)
controller_tournoi.add_tournament_player_controller(player4)
controller_tournoi.add_tournament_player_controller(player5)
# controller_tournoi.add_tournament_player_controller(player6)

controller_tournoi.display_tournament_info_controler()
controller_tournoi.display_player_tournament_controler()

##***************************   SIMULATION  ********************************

##***************   round   ***********************

new_round = Round()
controller_round=RoundController(new_round)

new_match = Match(None, None, None, None)
controller_match= MatchController(new_match)



##********************  copie   **********************

if championnat.nombre__de_participant_pair():
    i = 1
    for personne in range(0, championnat.nombre_de_participants(), 2):  # creation de variable match123
        globals()[f'match{i}'] = Match(championnat[personne][0], championnat[personne][1], championnat[personne+1][0], championnat[personne+1][1])
        i += 1
else:#on retire le joueur pour creer match
    i = 1
    for personne in range(0, championnat.nombre_de_participants()-1, 2):  # creation de variable match123
        globals()[f'match{i}'] = Match(championnat[personne][0], championnat[personne][1], championnat[personne + 1][0],
                                       championnat[personne + 1][1])
        i += 1
##*********************     copie   *****************************************


for tour in range(championnat.get_numbers_round()):
    print(f'************************Round numero {tour + 1}***************\n')
    championnat.increment_actual_round()
    list_round = []

    print("Affichage match:")
    for personne in range(1, championnat.nombre_de_participants() // 2 + 1):  # premier match
        print(globals()[f'match{personne}'])

    print()

    for personne in range(1, championnat.nombre_de_participants() // 2 + 1):  # simulation joueur gagnant
        globals()[f'match{personne}'].random_gagnant()
        globals()[f'new_match{personne}'] = Match(globals()[f'match{personne}'].player1,
                                                  globals()[f'match{personne}'].score1,
                                                  globals()[f'match{personne}'].player2,
                                                  globals()[f'match{personne}'].score2)
        list_round.append(globals()[f'new_match{personne}'])
        round = Round(list_round)
        round.set_numero(tour + 1)



    u = 1
    for personne in range(0, championnat.nombre_de_participants() // 2 + 2,
                          2):  # mise a jours des scores players du championnat
        championnat[personne][1] = globals()[f'new_match{u}'].score1
        # print(f"nombre de tour{championnat[0 + personne ][0]}")
        championnat[personne + 1][1] = globals()[f'new_match{u}'].score2
        # print(f"nombre de tour{ championnat[0 + personne+1 ][0] }")
        u = u + 1

    # trie des joueurs par score
    for personne in range(0,len(championnat)):
         championnat.tournament_players=sorted(championnat.tournament_players,key=lambda x: x[1],reverse=True)

    print( championnat.tournament_players)

##*******************************   paste   ***************************
    if championnat.nombre__de_participant_pair():
        i = 1
        for personne in range(0, championnat.nombre_de_participants(), 2):  # creation de variable match123
            globals()[f'match{i}'] = Match(championnat[personne][0], championnat[personne][1],
                                           championnat[personne + 1][0], championnat[personne + 1][1])
            i += 1
    else:  # on retire le joueur pour creer match
        i = 1
        for personne in range(0, championnat.nombre_de_participants() - 1, 2):  # creation de variable match123
            globals()[f'match{i}'] = Match(championnat[personne][0], championnat[personne][1],
                                           championnat[personne + 1][0],
                                           championnat[personne + 1][1])
            i += 1
## *************************************    paste   *********************************

    championnat.add_list_tournament_round(round)
    print()

print("*************************Fin du championnat****************************\n")
controller_tournoi.display_player_tournament_controler()
print()
print(championnat.list_round)

