# from controllers.menu_controllers import ApplicationController
#
# if __name__ == "__main__":
#     app = ApplicationController()
#     app.start()

import models
import views
import controllers

from datetime import date, timedelta

if __name__ == "__main__":

    player1 = models.player.Player("Dupont", "Adrien", date(1990, 5, 15), 50)
    player2 = models.player.Player("Moline", "Séverine", date(1992, 2, 1), 500)
    player3 = models.player.Player("Kagon", "Nino", date(1988, 11, 4), 350)
    player4 = models.player.Player("Guyot", "Maxime", date(1998, 3, 27), 400)
    player5 = models.player.Player("Dalco", "Lucien", date(1995, 8, 12), 500)
    player6 = models.player.Player("Vardie", "Jennifer", date(1995, 7, 21), 275)
    player7 = models.player.Player("Dupont", "Adrien", date(1990, 5, 15), 50)

    date_start = date(2023, 10, 14)
    date_end = date_start + timedelta(4)

    Championnat = models.tournament.Tournament("championnat académique", "Cergy", date_start, date_end)
    print(Championnat)

    controller_tournoi= models.tournament.TournamentController(Championnat)

    controller_tournoi.add_tournament_player(player1)
    controller_tournoi.add_tournament_player(player2)
    controller_tournoi.add_tournament_player(player3)
    controller_tournoi.add_tournament_player(player4)

    controller_tournoi.display_player_controller()


