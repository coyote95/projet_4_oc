from tinydb import TinyDB, Query
import os


class Player:
    def __init__(self, name, surname, birthday, id_chess="AB12345", score=0):
        self._name = name
        self._surname = surname
        self._birthday = birthday
        self.id_chess = id_chess
        self.score = score

    def __str__(self):
        return (
            f"Nom: {self._name} "
            f"Surname: {self._surname} "

        )

    def __repr__(self):
        return (
            f"Nom: {self._name} "
            f"Surname: {self._surname}"
        )

    def save_player_to_json(self, filename, table_name,score=True):
        db = TinyDB(filename)
        table = db.table(table_name)

        directory = os.path.dirname(filename)
        if not os.path.exists(directory):
            os.makedirs(directory)

        Recherche = Query()
        existing_player = table.get(
            (Recherche.name == self._name) &
            (Recherche.surname == self._surname) &
            (Recherche.id_chess == self.id_chess)
        )
        if existing_player:
            print(f"ERROR: {self._name} {self._surname} existe déjà dans le fichier{filename}.")
        else:
            # Aucun joueur avec les mêmes informations, vous pouvez ajouter le nouveau joueur
            if score==True:
                table.insert(self.dictionnary_player_score())
            else:
                table.insert(self.dictionnary_player())
            print(f"SAVE: {self._name} {self._surname} dans le fichier {filename}")
        db.close()

    def get_name(self):
        return self._name

    def get_surname(self):
        return self._surname

    def get_birthday(self):
        return self._birthday

    def get_id_chess(self):
        return self.id_chess

    def dictionnary_player_score(self):
        return {"name": self._name, "surname": self._surname, "birthday": self._birthday,
                "id_chess": self.id_chess, "score": self.score}

    def dictionnary_player(self):
        return {"name": self._name, "surname": self._surname, "birthday": self._birthday,
                "id_chess": self.id_chess}

    def set_name(self, name):
        self._name = name

    def set_surname(self, surname):
        self._surname = surname

    def set_birthday(self, birthday):
        self._birthday = birthday

    def set_id(self, id_chess):
        self.id_chess = id_chess

    @staticmethod
    def from_tinydb(numero, name_table="save_players", filename='./tournoi/players.json', score=True):
        db = TinyDB(filename)
        player_data = db.table(name_table).get(doc_id=numero)
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
    def from_tinydb_all(filename='./tournoi/players.json', name_table="save_players", score=True):
        db = TinyDB(filename)
        doc_ids = db.table(name_table).all()
        list_player = []
        for doc_id in doc_ids:
            new_player = Player.from_tinydb(doc_id.doc_id, name_table, filename, score)
            list_player.append(new_player)
        return list_player
