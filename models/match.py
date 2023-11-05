from tinydb import TinyDB, Query
import random
import os


class Match:
    def __init__(self, player1, player2, score1=0, score2=0, date_save=0):
        self.player1 = player1
        self.player2 = player2
        self.score1 = score1
        self.score2 = score2
        self.date_save = date_save

    def __str__(self):
        return (
            f"{self.player1} (score:{self.score1}) "
            f"CONTRE "
            f"{self.player2} (score: {self.score2})"
        )

    def __repr__(self):
        return (
            f"Match: "
            f"{self.player1} (score:{self.score1}) "
            f"CONTRE "
            f"{self.player2} (score: {self.score2})"
        )

    def save_round_to_json(self, filename="save_match"):
        db = TinyDB(filename)
        db.insert(self.dictionnary_match())

    def dictionnary_match(self):
        return {"date_save": self.date_save,
                "player1": self.player1.dictionnary_player_score(),
                "score1": self.score1,
                "player2": self.player2.dictionnary_player_score(),
                "score2": self.score2}

    def random_color(self):
        color = random.choice(["blanc", "noir"])
        self.player1.color = color
        if self.player1.color == "blanc":
            self.player2.color = "noir"
        else:
            self.player2.color = "blanc"

    def player1_winner(self):
        self.score1 += 1

    def player2_winner(self):
        self.score2 += 1

    def draw_match(self):
        self.score1 += 0.5
        self.score2 += 0.5

    def winner(self, winning_player):
        if winning_player == self.player1:
            self.player1_winner()
        elif winning_player == self.player2:
            self.player2_winner()
        elif winning_player == "execo":
            self.draw_match()


    @staticmethod
    def from_tinydb_list_match_round(list_matchs_docs_id):
        if isinstance(list_matchs_docs_id, int):
            list_matchs_docs_id = [list_matchs_docs_id]
        if list_matchs_docs_id:
            list_matchs = []
            for doc_id in list_matchs_docs_id:
                new_match = Match.from_tinydb(doc_id,
                                              filename='./data/matchs.json')
                list_matchs.append(new_match)
            return list_matchs
        else:
            return None

    @staticmethod
    def from_tinydb(numero, filename='./data/matchs.json'):
        db = TinyDB(filename)
        match_data = db.get(doc_id=numero)
        if match_data:
            return Match(
                match_data["player1"]["name"],
                match_data["player2"]["name"],
                match_data['score1'],
                match_data['score2'],
            )
        else:
            return None

    def save_match_to_json(self, filename="./data/matchs.json"):
        directory = os.path.dirname(filename)
        if not os.path.exists(directory):
            os.makedirs(directory)
        db = TinyDB(filename)
        db.insert(self.dictionnary_match())
        db.close()

    def find_doc_id_match(self, filename='./data/matchs.json'):
        directory = os.path.dirname(filename)
        if not os.path.exists(directory):
            os.makedirs(directory)
        db = TinyDB(filename)
        search = Query()
        result = db.search((search.player1.name == self.player1.name) &
                           (search.player1.surname == self.player1.surname) &
                           (search.player2.name == self.player2.name) &
                           (search.player2.surname == self.player2.surname) &
                           (search.date_save == self.date_save))
        if result:
            doc_id = result[0].doc_id
            db.close()
            return doc_id
        else:
            db.close()
            return None
