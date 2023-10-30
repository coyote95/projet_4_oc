from tinydb import TinyDB, Query
import os


class Player:
    def __init__(self, name, surname, birthday, id_chess="AB12345", score=0):
        self.name = name
        self.surname = surname
        self.birthday = birthday
        self.id_chess = id_chess
        self.score = score
        self.is_paired = False

    def __str__(self):
        return (
            f"Nom: {self.name} "
            f"Surname: {self.surname} "

        )

    def __repr__(self):
        return (
            f"Nom: {self.name} "
            f"Surname: {self.surname}"
        )

    def save_player_to_json(self, filename, table_name, score=True):
        db = TinyDB(filename)
        table = db.table(table_name)

        directory = os.path.dirname(filename)
        if not os.path.exists(directory):
            os.makedirs(directory)

        Recherche = Query()
        existing_player = table.get(
            (Recherche.name == self.name) &
            (Recherche.surname == self.surname) &
            (Recherche.id_chess == self.id_chess)
        )
        if existing_player:
            print(f"ERROR: {self.name} {self.surname} existe déjà dans le fichier{filename}.")
        else:
            # Aucun joueur avec les mêmes informations, vous pouvez ajouter le nouveau joueur
            if score == True:
                table.insert(self.dictionnary_player_score())
            else:
                table.insert(self.dictionnary_player())
            print(f"SAVE: {self.name} {self.surname} dans le fichier {filename}")
        db.close()

    def get_name(self):
        return self.name

    def get_surname(self):
        return self.surname

    def get_birthday(self):
        return self.birthday

    def get_id_chess(self):
        return self.id_chess

    def dictionnary_player_score(self):
        return {"name": self.name, "surname": self.surname, "birthday": self.birthday,
                "id_chess": self.id_chess, "score": self.score}

    def dictionnary_player(self):
        return {"name": self.name, "surname": self.surname, "birthday": self.birthday,
                "id_chess": self.id_chess}

    def set_name(self, name):
        self.name = name

    def set_surname(self, surname):
        self.surname = surname

    def set_birthday(self, birthday):
        self.birthday = birthday

    def set_id(self, id_chess):
        self.id_chess = id_chess

    @staticmethod
    def from_tinydb(numero, filename='./data/all_players.json', score=True):
        db = TinyDB(filename)
        player_data = db.get(doc_id=numero)
        if player_data:
            if score == True:
                return Player(
                    player_data['name'],
                    player_data['surname'],
                    player_data['birthday'],
                    player_data['id_chess'],
                    player_data['score']
                )
            else:
                return Player(
                    player_data['name'],
                    player_data['surname'],
                    player_data['birthday'],
                    player_data['id_chess'],
                )
        else:
            return None

    @staticmethod
    def from_tinydb_all(filename='./tournoi/players.json', score=True):
        db = TinyDB(filename)
        doc_ids = db.all()
        list_player = []
        for doc_id in doc_ids:
            new_player = Player.from_tinydb(doc_id.doc_id, filename, score)
            list_player.append(new_player)
        return list_player

    @staticmethod
    def from_tinydb_list_player_tournement(list_player_docs_id, filename='./tournoi/tournaments.json', score=False):
        if isinstance(list_player_docs_id, int):
            list_player_docs_id = [list_player_docs_id]

        if list_player_docs_id:
            list_player = []
            for doc_id in list_player_docs_id:
                new_player = Player.from_tinydb(doc_id, filename='./data/all_players.json ', score=score)
                list_player.append(new_player)
            return list_player
        else:
            return None

    def find_doc_id_player(self, filename='./data/all_players.json'):
        directory = os.path.dirname(filename)
        if not os.path.exists(directory):
            os.makedirs(directory)
        db = TinyDB(filename)
        Recherche = Query()
        result = db.search((Recherche.name == self.name) & (Recherche.surname == self.surname))
        if result:
            doc_id = result[0].doc_id
            db.close()
            return doc_id
        else:
            db.close()
            return None

    def pair(self):
        # Méthode pour appairer un joueur
        self.is_paired = True

    def unpair(self):
        # Méthode pour désappairer un joueur (par exemple, à la fin d'un round)
        self.is_paired = False
