from tinydb import TinyDB, Query
from models.match import Match
import os


class Round:
    def __init__(self,name='Round',numero_round=1,commence= "date de debut",termine= "date de fin",list_matchs=[]):
        self.name = name
        self.numero_round = numero_round
        self.commence = commence
        self.termine = termine
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

    def get_commence(self):
        return self.commence

    def get_termine(self):
        return self.termine

    def get_numero_round(self):
        return self.numero_round

    def set_match(self, list):
        self.matchs = list

    def set_numero(self, num):
        self.numero_round = num

    def set_commence(self,commence):
        self.commence = commence

    def set_termine(self, termine):
        self.termine = termine

    def add_match(self, match):
        return self.matchs.append(match)

    def save_round_to_json(self, filename="./data/rounds.json"):
        db = TinyDB(filename)

        directory = os.path.dirname(filename)
        if not os.path.exists(directory):
            os.makedirs(directory)

        Recherche = Query()
        existing_round = db.get(
            (Recherche.name == self.name) &
            (Recherche.numero_round == self.numero_round) &
            (Recherche.debut == self.commence)
        )
        if existing_round:
            print(f"ERROR: {self.name} {self.commence} existe déjà dans le fichier{filename}.")
        else:
            db.insert(self.dictionnary_round())
            print(f"SAVE: {self.name} {self.commence} dans le fichier {filename}")
        db.close()

    def dictionnary_round(self):
        matchs_data = [match.dictionnary_match() for match in self.matchs]
        return {"name": self.name, "numero_round": self.numero_round,"debut":self.commence,"fin":self.termine, "matchs": matchs_data}


    @staticmethod
    def from_tinydb_list_round_tournement(list_round_docs_id,filename='./data/rounds.json'):
        print (f"test: {list_round_docs_id}")
        if list_round_docs_id:
            list_round = []
            for doc_id in list_round_docs_id:
                new_round = Round.from_tinydb(doc_id,  filename='./data/rounds.json ')
                list_round.append(new_round)
            return list_round
        else:
            return None

    # @staticmethod
    # def from_tinydb_all(filename='./data/rounds.json'):
    #     db = TinyDB(filename)
    #     doc_ids = db.all()
    #     list_round = []
    #     for doc_id in doc_ids:
    #         new_player = Round.from_tinydb(doc_id.doc_id,  filename)
    #         list_round.append(new_player)
    #     return list_round

    @staticmethod
    def from_tinydb(numero,  filename='./data/rounds.json'):
        db = TinyDB(filename)
        print(numero)
        round_data = db.get(doc_id=numero)

        if round_data:
                return Round(
                    round_data['name'],
                    round_data['numero_round'],
                    round_data['debut'],
                    round_data['fin'],
                    #round_data['matchs']
                )

        else:
            return None

    def find_doc_id_round(self,filename='./data/rounds.json'):
        directory = os.path.dirname(filename)
        print(f"testttttttt:       {self.name}")
        if not os.path.exists(directory):
            print(f"PASSSSSS BONNNN")
            os.makedirs(directory)
        db = TinyDB(filename)
        Recherche = Query()
        result = db.search((Recherche.name == self.name) & (Recherche.numero_round == self.numero_round)& (Recherche.debut == self.commence))
        if result:
            doc_id = result[0].doc_id
            print(f"le doc id du round est{doc_id}")
            db.close()
            return doc_id
        else:
            print(f"le round{self.name}={Recherche.name} n'existe pas!")
            db.close()
            return None
