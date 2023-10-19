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

    def __getitem__(self, choice):  # tournament[0]
        return self.tournament_players[choice]

    def get_tournament_players(self):
        return self.tournament_players

    def nombre_de_participants(self):
        return len(self.tournament_players)

    def get_numbers_round(self):
        return self.numbers_round

    def get_round(self, choice):
        return self.list_round[choice]

    def add_tournament_player(self, player, score=0):
        list = [player, score]
        self.tournament_players.append(list)
        # self.tournament_players.append({"Player": player, "Score": score})

    # def new_score(self,player,score):
    #     self.[player][score]

    def update_tournament_player(self, player, score):
        self.get_tournament_players()

    def add_list_tournament_round(self, round):
        self.list_round.append(round)

    def new_date_start(self, date_start):
        self.date_start = date_start

    def new_date_end(self, date_end):
        self.date_end = date_end

    def increment_actual_round(self):
        self.actual_round += 1

    def new_name(self, name):
        self.name = name

    def new_place(self, place):
        self.place = place
