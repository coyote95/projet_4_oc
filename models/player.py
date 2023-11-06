import os

from tinydb import Query, TinyDB


class Player:
    def __init__(self, name, surname, birthday, id_chess="AB12345", score=0):
        self.name = name
        self.surname = surname
        self.birthday = birthday
        self.id_chess = id_chess
        self.score = score
        self.color = "blanc"

    def __str__(self):
        return f"Nom: {self.name} " f"Surname: {self.surname} "

    def __repr__(self):
        return f"Nom: {self.name} " f"Surname: {self.surname}"

    def get_name(self):
        return self.name

    def get_surname(self):
        return self.surname

    def get_birthday(self):
        return self.birthday

    def get_id_chess(self):
        return self.id_chess

    def set_name(self, name):
        self.name = name

    def set_surname(self, surname):
        self.surname = surname

    def set_birthday(self, birthday):
        self.birthday = birthday

    def set_id(self, id_chess):
        self.id_chess = id_chess

    def save_player_to_json(self, filename, score=True):
        directory = os.path.dirname(filename)
        if not os.path.exists(directory):
            os.makedirs(directory)
        db = TinyDB(filename)
        search = Query()
        existing_player = db.get(
            (search.name == self.name)
            & (search.surname == self.surname)
            & (search.id_chess == self.id_chess)
        )
        if existing_player:
            print("DEBUG")
            print(
                f"ERROR: {self.name} {self.surname} "
                f"existe déjà dans le fichier{filename}."
            )
        else:
            if score:
                db.insert(self.dictionnary_player_score())
            else:
                db.insert(self.dictionnary_player())
            print("DEBUG")
            print(f"SAVE: {self.name} {self.surname} dans le fichier {filename}")
        db.close()

    def dictionnary_player_score(self):
        return {
            "name": self.name,
            "surname": self.surname,
            "id_chess": self.id_chess,
            "score": self.score,
            "color": self.color,
        }

    def dictionnary_player(self):
        return {
            "name": self.name,
            "surname": self.surname,
            "birthday": self.birthday,
            "id_chess": self.id_chess,
        }

    @staticmethod
    def from_tinydb(numero, filename="./data/all_players.json", score=True):
        """
        Create a Player object from data in a TinyDB database.

        Parameters:
        - numero: An integer representing the unique document ID in the TinyDB database.
        - filename: (Optional) The path to the TinyDB database file. Defaults to "./data/all_players.json".
        - score: (Optional) A boolean indicating whether to include the player's score. Defaults to True.

        Returns:
        - A Player object created from the data in the TinyDB document with the
         specified ID, or None if the document is not found.

        """
        db = TinyDB(filename)
        player_data = db.get(doc_id=numero)
        if player_data:
            if score:
                return Player(
                    player_data["name"],
                    player_data["surname"],
                    player_data["birthday"],
                    player_data["id_chess"],
                    player_data["score"],
                )
            else:
                return Player(
                    player_data["name"],
                    player_data["surname"],
                    player_data["birthday"],
                    player_data["id_chess"],
                )
        else:
            return None

    @staticmethod
    def from_tinydb_all(filename="./tournoi/players.json", score=True):
        """
        Create a list of Player objects from data in all documents in a TinyDB database.

        Parameters:
        - filename: (Optional) The path to the TinyDB database file. Defaults to "./tournoi/players.json".
        - score: (Optional) A boolean indicating whether to include the player's score. Defaults to True.

        Returns:
        - A list of Player objects created from the data in all documents in the TinyDB database,
         or an empty list if no documents are found.
        """
        db = TinyDB(filename)
        doc_ids = db.all()
        list_player = []
        for doc_id in doc_ids:
            new_player = Player.from_tinydb(doc_id.doc_id, filename, score)
            list_player.append(new_player)
        return list_player

    @staticmethod
    def from_tinydb_list_player_tournement(list_player_docs_id, score=False):
        """
        Create a list of Player objects from TinyDB documents based on their IDs for a tournament.

        Parameters:
        - list_player_docs_id: An integer or a list of integers representing document IDs in the TinyDB database.
        - score: (Optional) A boolean indicating whether to include the player's score. Defaults to False.

        Returns:
        - A list of Player objects created from the TinyDB documents with the specified IDs,
         or None if the input list is empty.

        If a single integer is provided as the input, it is automatically converted into a list with one element.
        """
        if isinstance(list_player_docs_id, int):
            list_player_docs_id = [list_player_docs_id]
        if list_player_docs_id:
            list_player = []
            for doc_id in list_player_docs_id:
                new_player = Player.from_tinydb(
                    doc_id, filename="./data/all_players" ".json ", score=score
                )
                list_player.append(new_player)
            return list_player
        else:
            return None

    def find_doc_id_player(self, filename="./data/all_players.json"):
        """
        Find the document ID of a player in the TinyDB database based on their name and surname.

        Parameters:
        - filename: (Optional) The path to the TinyDB database file. Defaults to "./data/all_players.json".

        Returns:
        - The document ID of the player in the TinyDB database with matching name and surname,
         or None if no matching document is found.

        This method searches for a player in the TinyDB database by matching
        their name and surname. If a matching document is found, its document ID is returned.
        If no matching document is found, None is returned.
        """
        directory = os.path.dirname(filename)
        if not os.path.exists(directory):
            os.makedirs(directory)
        db = TinyDB(filename)
        search = Query()
        result = db.search(
            (search.name == self.name) & (search.surname == self.surname)
        )
        if result:
            doc_id = result[0].doc_id
            db.close()
            return doc_id
        else:
            db.close()
            return None
