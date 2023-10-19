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
championnat = Tournament("championnat académique", "Cergy", date_start, date_end, 4)
print(championnat)

model = championnat
view = TournamentView(model)  # appeler la vue du model
controller_tournoi = TournamentController(model, view)
controller_tournoi.add_tournament_player_controller(player1)
controller_tournoi.add_tournament_player_controller(player2)
controller_tournoi.add_tournament_player_controller(player3)
controller_tournoi.add_tournament_player_controller(player4)
controller_tournoi.add_tournament_player_controller(player5)
controller_tournoi.add_tournament_player_controller(player6)
controller_tournoi.display_player_tournament_controler()

######round####

new_round = Round()
new_match = Match(None, None, None, None)
model_round = new_round
model_match = new_match

print()

list_player = championnat.get_tournament_players()
print(f"Nombre de tour total:{championnat.get_numbers_round()}\n")

for personne in range(0, championnat.nombre_de_participants()):
    globals()[f'P{personne}'] = championnat[0 + personne][0]
    globals()[f'S{personne}'] = championnat[0 + personne][1]

i = 1
for personne in range(0, championnat.nombre_de_participants(), 2):
    globals()[f'match{i}'] = Match(globals()[f'P{personne}'], S1, globals()[f'P{personne + 1}'], S2)
    i += 1

for personne in range(1, championnat.nombre_de_participants() // 2 + 1):
    print(globals()[f'match{personne}'])

#################programmation########################


print(f"nombre de participant{championnat.nombre_de_participants()}\n")

for tour in range(championnat.get_numbers_round()):

    print(f'************************Round numero {tour + 1}***************')
    championnat.increment_actual_round()
    list_round = []

    for personne in range(1, championnat.nombre_de_participants() // 2 + 1):
        globals()[f'match{personne}'].random_gagnant()
        globals()[f'new_match{personne}'] = Match(globals()[f'match{personne}'].player1,
                                                  globals()[f'match{personne}'].score1,
                                                  globals()[f'match{personne}'].player2,
                                                  globals()[f'match{personne}'].score2)
        list_round.append(globals()[f'new_match{personne}'])
        round = Round(list_round)
        round.new_numero(tour)

    u=1
    for personne in range(0, championnat.nombre_de_participants()//2+2,2):
        championnat[0 + personne][1] = globals()[f'new_match{u}'].score1
        print(f"nombre de tour{championnat[0 + personne ][0]}")
        championnat[0 + personne+1 ][1] = globals()[f'new_match{u}'].score2
        print(f"nombre de tour{ championnat[0 + personne+1 ][0] }")
        u=u+1

    controller_tournoi.display_player_tournament_controler()

    championnat.add_list_tournament_round(round)

print(championnat.list_round[0])
print(championnat.list_round[1])
print(championnat.list_round[2])
controller_tournoi.display_player_tournament_controler()
#championnat[0][1] = 5


print()
controller_tournoi.display_player_tournament_controler()
