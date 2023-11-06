import os

from tinydb import Query, TinyDB

from models.match import Match


class Round:
    def __init__(self, name="Round", numero_round=0, date_save=0, list_matchs=None):
        if list_matchs is None:
            list_matchs = []
        self.name = name
        self.numero_round = numero_round
        self.date_save = date_save
        self.matchs = list_matchs

    def __str__(self):
        return f"Numero du round: {self.numero_round} " f"matchs: {self.matchs}"

    def __repr__(self):
        return f"Numero du round: {self.numero_round} " f"matchs: {self.matchs}"

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
        """
        Save the match round data, including a list of match document IDs, to a TinyDB database.

        Parameters:
        - filename: The path to the TinyDB database file where the match round data will be saved.

        This method creates or updates a record in the TinyDB database for the tournament, including the
         list of document IDs of the matches associated with the tournament.
        If a record for the tournament already exists, it is updated; otherwise, a new record is created.
        The record is identified based on the tournament name, round number, and date of save.
        """
        directory = os.path.dirname(filename)
        if not os.path.exists(directory):
            os.makedirs(directory)
        list_matchs = []
        for match in self.matchs:
            if isinstance(match, Match):
                list_matchs.append(match.find_doc_id_match())
        db = TinyDB(filename)
        recherche = Query()
        result = db.search(
            (recherche.name == self.name)
            & (recherche.numero_round == self.numero_round)
            & (recherche.date_save == self.date_save)
        )
        if result:
            doc_id = result[0].doc_id
            db.update({"list_doc_id_matchs": list_matchs}, doc_ids=[doc_id])
        else:
            print("DEBUG")
            print("ERROR: Le tournoi n'existe pas!")
        db.close()

    def dictionnary_round(self):
        return {
            "date_save": self.date_save,
            "name": self.name,
            "numero_round": self.numero_round,
            "list_doc_id_matchs": None,
        }

    @staticmethod
    def from_tinydb_list_round_tournement(list_round_docs_id):
        """
        Create a list of Round objects from TinyDB documents based on their IDs for a tournament.

        Parameters:
        - list_round_docs_id: A list of integers representing document IDs in the TinyDB database.

        Returns:
        - A list of Round objects created from the TinyDB documents with the specified IDs,
         or None if the input list is empty.
        """
        if list_round_docs_id:
            list_round = []
            for doc_id in list_round_docs_id:
                new_round = Round.from_tinydb(doc_id, filename="./data/rounds.json ")
                list_round.append(new_round)
            return list_round
        else:
            return None

    @staticmethod
    def from_tinydb(numero, filename="./data/rounds.json"):
        """
        Create a Round object from data in a TinyDB database using its unique document ID.

        Parameters:
        - numero: An integer representing the unique document ID in the TinyDB database.
        - filename: (Optional) The path to the TinyDB database file. Defaults to "./data/rounds.json".

        Returns:
        - A Round object created from the data in the TinyDB document with the specified ID, or None if the
         document is not found.

        This method retrieves round data from the TinyDB database using the specified document ID.
         It then creates a Round object based on the retrieved data, including attributes like name, round number,
          date of save, and a list of associated match document IDs.
        If the document is not found, None is returned.
        """
        db = TinyDB(filename)
        round_data = db.get(doc_id=numero)
        if round_data:
            return Round(
                round_data["name"],
                round_data["numero_round"],
                round_data["date_save"],
                Match.from_tinydb_list_match_round(round_data["list_doc_id_matchs"]),
            )
        else:
            return None

    def find_doc_id_round(self, filename="./data/rounds.json"):
        """
        Find the document ID of a round in the TinyDB database based on its attributes.

        Parameters:
        - filename: (Optional) The path to the TinyDB database file. Defaults to "./data/rounds.json".

        Returns:
        - The document ID of the round in the TinyDB database with matching attributes, or None if no matching
         document is found.

        This method searches for a round in the TinyDB database by matching its name, round number, and date of save.
          If a matching document is found, its document ID is returned.
        If no matching document is found, None is returned.
        """
        directory = os.path.dirname(filename)
        if not os.path.exists(directory):
            os.makedirs(directory)
        db = TinyDB(filename)
        search = Query()
        result = db.search(
            (search.name == self.name)
            & (search.numero_round == self.numero_round)
            & (search.date_save == self.date_save)
        )
        if result:
            doc_id = result[0].doc_id
            db.close()
            return doc_id
        else:
            db.close()
            return None
