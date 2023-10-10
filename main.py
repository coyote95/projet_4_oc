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
    date_start = date(2023, 10, 14)
    date_end = date_start + timedelta(4)

    Tournoi = models.tournament.Tournament("championnat académique", "Cergy", date_start, date_end)
    print(Tournoi)
