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

    def add_tournament_player(self, player, score=0):
        self.tournament_players.append({"player": player, "score": score})

    def new_date_start(self, date_start):
        self.date_start = date_start

    def new_date_end(self, date_end):
        self.date_end = date_end

    def new_numbers_round(self, numbers_round):
        self.numbers_round = numbers_round

    def new_name(self, name):
        self.name = name

    def new_place(self, place):
        self.place = place
