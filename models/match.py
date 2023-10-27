import random
from tinydb import TinyDB, Query
from models.player import Player
import os


class Match:
    def __init__(self, player1, player2, score1=0, score2=0):
       # self.commence=commence
        self.player1 = player1
        self.player2 = player2
        self.score1 = score1
        self.score2 = score2


    def __str__(self):
        return (
            f"{self.player1} (score:{self.score1}) CONTRE {self.player2} (score: {self.score2})  "
        )

    def __repr__(self):
        return (
            f"Match: {self.player1} (score:{self.score1}) CONTRE {self.player2} (score: {self.score2})  "
        )

    def save_round_to_json(self, filename="save_match"):
        db = TinyDB(filename)
        db.insert(self.dictionnary_match())

    def dictionnary_match(self):
        return {"player1": self.player1.__dict__, "score1": self.score1, "player2": self.player2.__dict__,
                "score2": self.score2}

    def player1_gagnant(self):
        self.score1 += 1

    def player2_gagnant(self):
        self.score2 += 1

    def execo(self):
        self.score1 += 0.5
        self.score2 += 0.5

    def random_gagnant(self):
        choix_gagnant = random.choice([self.player1, self.player2, "execo"])
        if choix_gagnant == self.player1:
            print(f"le joueur gagant est:{choix_gagnant}")
            self.player1_gagnant()
        elif choix_gagnant == self.player2:
            print(f"le joueur gagant est:{choix_gagnant}")
            self.player2_gagnant()
        elif choix_gagnant == "execo":
            print(f"Match nul!!")
            self.execo()
        print(f"Nouveau score: {self.player1} (score:{self.score1}) CONTRE {self.player2} (score: {self.score2})\n ")
        return choix_gagnant

    @staticmethod
    def from_tinydb_list_match_round(list_matchs_docs_id, filename='./tournoi/tournaments.json'):
        if isinstance(list_matchs_docs_id, int):
            list_matchs_docs_id = [list_matchs_docs_id]

        if list_matchs_docs_id:
            print(f"list match doc id {list_matchs_docs_id}")
            list_matchs = []
            for doc_id in list_matchs_docs_id:
                print(doc_id)
                new_match = Match.from_tinydb(doc_id, filename='./data/matchs.json ')
                list_matchs.append(new_match)
            return list_matchs
        else:
            return None

    @staticmethod
    def from_tinydb(numero, filename='./data/matchs.json'):
        db = TinyDB(filename)
        print(numero)
        match_data = db.get(doc_id=numero)

        if match_data:
            return Match(
                Player.from_tinydb(match_data["player1"]),
                Player.from_tinydb(match_data["player2"]),
                match_data['score1'],
                match_data['score2'],
            )
        else:
            return None

    def save_match_to_json(self, filename="./data/matchss.json"):
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
        Recherche = Query()
        print(self.player1)

        result = db.search((Recherche.player1._name== self.player1._name) &
                            (Recherche.player1._surname== self.player1._surname) &
                           (Recherche.player2._name == self.player2._name) &
                           (Recherche.player2._surname == self.player2._surname) &
                           (Recherche.score1 == self.score1))

        print( self.player1._name)
        print(f"result{result}")
        if result:
            doc_id = result[0].doc_id
            db.close()
            return doc_id
        else:
            db.close()
            return None
