from models.player import Player
from models.tournament import Tournament
from models.menu import MenuEntry, Menu
from models.round import Round
from models.match import Match
from views.player_view import PlayerView
#from views.tournament_view import TournamentView
from views.menu_view import HomeMenuView
from views.round_view import RoundView
from views.match_view import MatchView
from controllers.player_controllers import PlayerController
from controllers.tournamenent_controllers import TournamentController
from controllers.menu_controllers import ApplicationController, HomeMenuController, MenuNewTournamentController
from controllers.round_controllers import RoundController
from controllers.match_controllers import MatchController
from datetime import date, timedelta, datetime
from tinydb import TinyDB, Query

app = ApplicationController()
app.start()

