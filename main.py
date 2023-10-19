from models.player import Player
from models.tournament import Tournament
from models.menu import MenuEntry, Menu
from models.round_match import Round, Match
from views.player_view import PlayerView
from views.tournament_view import TournamentView
from views.menu_view import HomeMenuView
from views.round_match_view import RoundView, MatchView
from controllers.player_controllers import PlayerController
from controllers.tournamenent_controllers import TournamentController
from controllers.menu_controllers import ApplicationController, HomeMenuController, MenuNewTournamentController
from controllers.round_match_controllers import RoundMatchController

from datetime import date, timedelta
from tinydb import TinyDB, Query

########Menu
# app = ApplicationController()
# app.start()
# menu = Menu()
#
#
# newtournament = Tournament(None,None,None,None)
# model = newtournament
# view = TournamentView(model)  # appeler la vue du model
# controller_tournoi = TournamentController(model, view)
# controller_tournoi.creation_tournoi()
# print(model)
#
#
# for tentative in range(2):
#     print(f"Player {tentative+1}")
#     newplayer=Player(None,None,None,None)
#     model=newplayer
#     view=PlayerView()
#     controller_player=PlayerController(model,view)
#     controller_player.creation_player()
#     print(f"Resume:{model}\n")
#     controller_tournoi.add_tournament_player_controller(model)
#
#
# controller_tournoi.display_player_tournament_controler()


###########  player    ##############"

player1 = Player("Dupont", "Adrien", date(1990, 5, 15), 50)
player2 = Player("Moline", "Séverine", date(1992, 2, 1), 500)
player3 = Player("Kagon", "Nino", date(1988, 11, 4), 350)
player4 = Player("Guyot", "Maxime", date(1998, 3, 27), 400)
player5 = Player("Dalco", "Lucien", date(1995, 8, 12), 500)
player6 = Player("Vardie", "Jennifer", date(1995, 7, 21), 275)
player7 = Player("Dupont", "Adrien", date(1990, 5, 15), 50)

# db = TinyDB("Players.json")
# db.truncate()

# view = PlayerView()

# controller = PlayerController(player1, view)
# #controller.save_player_controller("Players.json")
# controller.display_player_controller()
#
# controller = PlayerController(player2, view)
# controller.save_player_controller("Players.json")
# controller.display_player_controller()
#
# controller = PlayerController(player3, view)
# controller.save_player_controller("Players.json")
# controller.display_player_controller()
#
# controller = PlayerController(player4, view)
# controller.save_player_controller("Players.json")
# controller.display_player_controller()
#
# controller.display_db("Players.json")

#################     TOURNOI     ###########

date_start = date(2023, 10, 14)
date_end = date_start + timedelta(4)
championnat = Tournament("championnat académique", "Cergy", date_start, date_end, 6)
print(championnat)

model = championnat
view = TournamentView(model)  # appeler la vue du model
controller_tournoi = TournamentController(model, view)
controller_tournoi.add_tournament_player_controller(player1)
controller_tournoi.add_tournament_player_controller(player2)
controller_tournoi.add_tournament_player_controller(player3)
controller_tournoi.add_tournament_player_controller(player4)
controller_tournoi.add_tournament_player_controller(player5)
# controller_tournoi.add_tournament_player_controller(player6)
controller_tournoi.display_player_tournament_controler()

######round####

new_round = Round()
new_match = Match(None, None, None, None)
model_round = new_round
model_match = new_match

print()

list_player = championnat.get_tournament_players()
print(f"Nombre de tour total:{championnat.get_numbers_round()}")


#####copie#####
for personne in range(0, championnat.nombre_de_participants()):  # affectation des players du championnat à P123
    globals()[f'P{personne}'] = championnat[0 + personne][0]  # affectation des players du championnat à S123
    globals()[f'S{personne}'] = championnat[0 + personne][1]


if championnat.nombre__de_participant_pair():
    i = 1
    for personne in range(0, championnat.nombre_de_participants(), 2):  # creation de variable match123
        globals()[f'match{i}'] = Match(globals()[f'P{personne}'], S1, globals()[f'P{personne + 1}'], S2)
        i += 1
else:#on retire le joueur pour creer match
    i = 1
    for personne in range(0, championnat.nombre_de_participants()-1, 2):  # creation de variable match123
        globals()[f'match{i}'] = Match(globals()[f'P{personne}'], S1, globals()[f'P{personne + 1}'], S2)
        i += 1
####copie#####


print(f"nombre de participant:{championnat.nombre_de_participants()}\n")

print("Premier match:")
for personne in range(1, championnat.nombre_de_participants() // 2 + 1):  # premier match
    print(globals()[f'match{personne}'])

print()

for tour in range(championnat.get_numbers_round()):
    print(f'************************Round numero {tour + 1}***************\n')
    championnat.increment_actual_round()
    list_round = []

    for personne in range(1, championnat.nombre_de_participants() // 2 + 1):  # simulation joueur gagnant
        globals()[f'match{personne}'].random_gagnant()
        globals()[f'new_match{personne}'] = Match(globals()[f'match{personne}'].player1,
                                                  globals()[f'match{personne}'].score1,
                                                  globals()[f'match{personne}'].player2,
                                                  globals()[f'match{personne}'].score2)
        list_round.append(globals()[f'new_match{personne}'])
        round = Round(list_round)
        round.new_numero(tour+1)



    u = 1
    for personne in range(0, championnat.nombre_de_participants() // 2 + 2,
                          2):  # mise a jours des scores players du championnat
        championnat[0 + personne][1] = globals()[f'new_match{u}'].score1
        # print(f"nombre de tour{championnat[0 + personne ][0]}")
        championnat[0 + personne + 1][1] = globals()[f'new_match{u}'].score2
        # print(f"nombre de tour{ championnat[0 + personne+1 ][0] }")
        u = u + 1

    # trie des joueurs par score
    for personne in range(0,len(championnat)):
         championnat.tournament_players=sorted(championnat.tournament_players,key=lambda x: x[1],reverse=True)

    print( championnat.tournament_players)

    #####copie#####
    for personne in range(0, championnat.nombre_de_participants()):  # affectation des players du championnat à P123
        globals()[f'P{personne}'] = championnat[0 + personne][0]  # affectation des players du championnat à S123
        globals()[f'S{personne}'] = championnat[0 + personne][1]

    if championnat.nombre__de_participant_pair():
        i = 1
        for personne in range(0, championnat.nombre_de_participants(), 2):  # creation de variable match123
            globals()[f'match{i}'] = Match(globals()[f'P{personne}'], S1, globals()[f'P{personne + 1}'], S2)
            i += 1
    else:  # on retire le joueur pour creer match
        i = 1
        for personne in range(0, championnat.nombre_de_participants() - 1, 2):  # creation de variable match123
            globals()[f'match{i}'] = Match(globals()[f'P{personne}'], S1, globals()[f'P{personne + 1}'], S2)
            i += 1
    ####copie#####



    championnat.add_list_tournament_round(round)
    print()

print("*************************Fin du championnat****************************\n")
controller_tournoi.display_player_tournament_controler()
print()
print(championnat.list_round)


