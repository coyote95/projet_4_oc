from tinydb import TinyDB, Query
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
            f"{self.player1} (score:{self.score1}) CONTRE {self.player2} (score: {self.score2})"
        )

    def __repr__(self):
        return (
            f"Match: {self.player1} (score:{self.score1}) CONTRE {self.player2} (score: {self.score2})"
        )

    def save_round_to_json(self, filename="save_match"):
        db = TinyDB(filename)
        db.insert(self.dictionnary_match())

    def dictionnary_match(self):
        return {"date_save": self.date_save, "player1": self.player1.__dict__, "score1": self.score1,
                "player2": self.player2.__dict__,
                "score2": self.score2}

    def player1_gagnant(self):
        self.score1 += 1

    def player2_gagnant(self):
        self.score2 += 1

    def execo(self):
        self.score1 += 0.5
        self.score2 += 0.5

    def vainqueuer(self, player_gagnant):
        print("dans la methode vainqueuer!!!!!")

        if player_gagnant == self.player1:
            print(f"le joueur gagant est:{player_gagnant}")
            self.player1_gagnant()
        elif player_gagnant == self.player2:
            print(f"le joueur gagant est:{player_gagnant}")
            self.player2_gagnant()
        elif player_gagnant == "execo":
            print(f"Match nul!!")
            self.execo()
        print(f"Nouveau score: {self.player1} (score:{self.score1}) CONTRE {self.player2} (score: {self.score2})\n ")

    @staticmethod
    def from_tinydb_list_match_round(list_matchs_docs_id):
        if isinstance(list_matchs_docs_id, int):
            list_matchs_docs_id = [list_matchs_docs_id]

        if list_matchs_docs_id:
            list_matchs = []
            for doc_id in list_matchs_docs_id:
                new_match = Match.from_tinydb(doc_id, filename='./data/matchs.json ')
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
                match_data["player1"]["_name"],
                match_data["player2"]["_name"],
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
        recherche = Query()

        result = db.search((recherche.player1.name == self.player1.name) &
                           (recherche.player1.surname == self.player1.surname) &
                           (recherche.player2.name == self.player2.name) &
                           (recherche.player2.surname == self.player2.surname) &
                           (recherche.date_save == self.date_save))

        if result:
            doc_id = result[0].doc_id
            db.close()
            return doc_id
        else:
            db.close()
            return None
