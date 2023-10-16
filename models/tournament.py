class Tournament:
    def __init__(self, name, place, date_start, date_end, numbers_round=4):
        self.name = name
        self.place = place
        self.date_start = date_start
        self.date_end = date_end
        self.numbers_round = numbers_round

        self.actual_round = 1
        self.list_round = []
        self.tournament_players = []  # liste de dictionnaire
        self.description = []

    def __str__(self):
        return (
            f"*********Tournoi*******\n"
            f" Nom: {self.name}: \n"
            f" Place: {self.place}\n"
            f" Date de debut: {self.date_start}\n"
            f" Date de fin: {self.date_end}\n"
        )

    def __repr__(self):
        return str(self)

    def get_tournament_players(self):
        return self.tournament_players


    # def display_player_controller(self):
    #     view = TournamentView(self.tournament)
    #     view.display_players_tournament()

    def add_tournament_player(self, player):
        self.tournament_players.append(player)

    # def get_players(self):
    #     return self.tournament.saving_players
    #
    # def add_tournament_controllers(self, tournament):
    #     self.tournament.append(tournament)
