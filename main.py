from models.player import Player
from models.tournament import Tournament
from models.menu import MenuEntry, Menu
from models.round_match import Round, Match
from views.player_view import PlayerView
from views.tournament_view import TournamentView
from views.menu_view import HomeMenuView
from views.round_match_view import RoundView,   MatchView
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

#db = TinyDB("Players.json")
#db.truncate()

#view = PlayerView()

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
Championnat = Tournament("championnat académique", "Cergy", date_start, date_end)
print(Championnat)

model = Championnat
view = TournamentView(model)  # appeler la vue du model
controller_tournoi = TournamentController(model, view)
controller_tournoi.add_tournament_player_controller(player1)
controller_tournoi.add_tournament_player_controller(player2)
controller_tournoi.add_tournament_player_controller(player3)
controller_tournoi.add_tournament_player_controller(player4)
controller_tournoi.display_player_tournament_controler()



######round####

new_round= Round(None)
new_match=Match(None,None,None,None)
model_round=new_round
model_match= new_match

print()

list_player=Championnat.get_tournament_players()
for tour in range(Championnat.get_numbers_round()):
    print(f"Nombre de tour total:{Championnat.get_numbers_round()}")
    print(f"Round {tour+1}:")
    player1=Championnat[0][0]
    score1=Championnat[0][1]
    player2=Championnat[1][0]
    score2 = Championnat[1][1]
    print(Championnat[0][1])#matrice tableau dans un tableau
    print(player1)
    print(score1)
    print(player2)
    print(score2)
    match1=Match(player1,score1,player2,score2)
    print(match1)



