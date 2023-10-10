class Tournament:
    def __init__(self, name, place, date_start, date_end, numbers_round=4):
        self.name = name
        self.place = place
        self.date_start = date_start
        self.date_end = date_end
        self.numbers_round = numbers_round

        self.actual_round = 1
        self.list_tours = []
        self.saving_players = []
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
        return (
            f"*********Tournoi*******\n"
            f" Nom: {self.name}: \n"
            f" Place: {self.place}\n"
            f" Date de debut: {self.date_start}\n"
            f" Date de fin: {self.date_end}\n"
        )
