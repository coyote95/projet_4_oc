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
Championnat = Tournament("championnat académique", "Cergy", date_start, date_end, 4)
print(Championnat)

model = Championnat
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

list_player = Championnat.get_tournament_players()
print(f"Nombre de tour total:{Championnat.get_numbers_round()}\n")

for personne in range(0, Championnat.nombre_de_participants()):
    globals()[f'P{personne}'] = Championnat[0 + personne][0]
    globals()[f'S{personne}'] = Championnat[0 + personne][1]

i = 1
for personne in range(0, Championnat.nombre_de_participants(), 2):
    globals()[f'match{i}'] = Match(globals()[f'P{personne}'], S1, globals()[f'P{personne + 1}'], S2)
    i += 1

for personne in range(1, Championnat.nombre_de_participants()//2+1):
    print( globals()[f'match{personne}'])



#################programmation########################


print(f"nombre de participant{Championnat.nombre_de_participants()}")

for tour in range(Championnat.get_numbers_round()):

    round = Round()
    print(P1)
    print(f'Round numero {tour + 1}')
    Championnat.increment_actual_round()

    for personne in range(1, Championnat.nombre_de_participants() // 2 + 1):
        globals()[f'match{personne}'].random_gagnant()
        round.add_match( globals()[f'match{personne}'])

    print (f'liste match{round.matchs}')








    # for i in range(1, 4):
    #     globals()[f'numero{i}'] = i



    # match1.random_gagnant()
    # match2.random_gagnant()

#     new_match_1=Match(match1.player1,match1.score1,match1.player2,match1.score2)
#     new_match_2 = Match(match2.player1, match2.score1, match2.player2, match2.score2)
#
#     round.new_match([new_match_1,new_match_2])
#     new_round=Round(round.matchs,(tour+1))
#
#     Championnat.add_list_tournament_round(new_round)
# print("*********FINALE********")
#
#
# print(Championnat.list_round)
#
#
