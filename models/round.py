from tinydb import TinyDB, Query
from models.match import Match
import os


class Round:
    def __init__(self, name="Round", numero_round=0, date_save=0, list_matchs=None):
        if list_matchs is None:
            list_matchs = []
        self.name = name
        self.numero_round = numero_round
        self.date_save = date_save
        self.matchs = list_matchs

    def __str__(self):
        return (
            f"Numero du round: {self.numero_round} "
            f"matchs: {self.matchs}"
        )

    def __repr__(self):
        return (
            f"Numero du round: {self.numero_round} "
            f"matchs: {self.matchs}"
        )

    def __getitem__(self, choice):  # Round[0]
        return self.matchs[choice]

    def get_match(self):
        return self.matchs

    def get_name(self):
        return self.name

    def get_date_save(self):
        return self.get_date_save()

    def get_numero_round(self):
        return self.numero_round

    def set_match(self, list_matchs):
        self.matchs = list_matchs

    def set_numero(self, num):
        self.numero_round = num

    def set_date_save(self, date):
        self.date_save = date

    def increment_numero_round(self):
        self.numero_round += 1

    def add_match(self, match):
        return self.matchs.append(match)

    def save_round_to_json(self, filename="./data/rounds.json"):
        db = TinyDB(filename)
        directory = os.path.dirname(filename)
        if not os.path.exists(directory):
            os.makedirs(directory)
        db.insert(self.dictionnary_round())

    def save_match_round_to_json(self, filename):
        directory = os.path.dirname(filename)
        if not os.path.exists(directory):
            os.makedirs(directory)
        list_matchs = []
        for match in self.matchs:
            if isinstance(match, Match):
                list_matchs.append(match.find_doc_id_match())
        db = TinyDB(filename)
        recherche = Query()
        result = db.search((recherche.name == self.name) & (recherche.numero_round == self.numero_round) & (
                recherche.date_save == self.date_save))
        if result:
            doc_id = result[0].doc_id
            db.update({"list_doc_id_matchs": list_matchs}, doc_ids=[doc_id])
        else:
            print("ERROR: Le tournoi n'existe pas!")
        db.close()

    def dictionnary_round(self):
        return {"date_save": self.date_save, "name": self.name, "numero_round": self.numero_round,
                "list_doc_id_matchs": None}

    @staticmethod
    def from_tinydb_list_round_tournement(list_round_docs_id):
        if list_round_docs_id:
            list_round = []
            for doc_id in list_round_docs_id:
                new_round = Round.from_tinydb(doc_id, filename='./data/rounds.json ')
                list_round.append(new_round)
            return list_round
        else:
            return None

    @staticmethod
    def from_tinydb(numero, filename='./data/rounds.json'):
        db = TinyDB(filename)
        round_data = db.get(doc_id=numero)
        if round_data:
            return Round(
                round_data['name'],
                round_data['numero_round'],
                round_data['date_save'],
                Match.from_tinydb_list_match_round(round_data["list_doc_id_matchs"])
            )
        else:
            return None

    def find_doc_id_round(self, filename='./data/rounds.json'):
        directory = os.path.dirname(filename)
        if not os.path.exists(directory):
            os.makedirs(directory)
        db = TinyDB(filename)
        search = Query()
        print(self.name)
        print(self.numero_round)
        result = db.search((search.name == self.name) & (search.numero_round == self.numero_round) &
                           (search.date_save == self.date_save))
        if result:
            doc_id = result[0].doc_id
            db.close()
            return doc_id
        else:
            db.close()
            return None
