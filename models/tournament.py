from tinydb import TinyDB, Query
from models.player import Player
import os

class Tournament:
    def __init__(self, name, place, date_start, date_end, numbers_round=4):
        self.name = name
        self.place = place
        self.date_start = date_start
        self.date_end = date_end
        self.numbers_round = numbers_round
        self.actual_round = 1
        self.list_round = []
        self.tournament_players = []  # liste de dictionnaire
        self.description = []

    def __str__(self):
        return (
            f"*********Tournoi*******\n"
            f"Nom: {self.name} \n"
            f"Place: {self.place}\n"
            f"Date de debut: {self.date_start}\n"
            f"Date de fin: {self.date_end}\n"
        )

    def __repr__(self):
        return str(self)

    def __getitem__(self, choice):  # tournament[0]
        return self.tournament_players[choice]

    def __len__(self):
        return len(self.tournament_players)

    def get_tournament_players(self):
        return self.tournament_players

    def get_numbers_round(self):
        return self.numbers_round

    def get_round(self, choice):
        return self.list_round[choice]

    def set_name(self, name):
        self.name = name

    def set_place(self, place):
        self.place = place

    def set_date_start(self, date_start):
        self.date_start = date_start

    def set_date_end(self, date_end):
        self.date_end = date_end

    def set_round(self, round):
        self.numbers_round = round


    def nombre__de_participant_pair(self):
        if len(self.tournament_players) % 2 == 0:
            return True
        else:
            return False

    def nombre_de_participants(self):
        return len(self.tournament_players)


    def add_tournament_player(self, player):
        self.tournament_players.append(player)

    def add_list_tournament_round(self, round):
        self.list_round.append(round)

    def increment_actual_round(self):
        self.actual_round += 1

    def save_player_tournament_to_json(self, filename='./tournoi/players.json'):
        directory=os.path.dirname(filename)
        if not os.path.exists(directory):
            os.makedirs(directory)
        db = TinyDB(filename)
        table=db.table("save_players")

        for player in self.tournament_players:
            if isinstance(player,Player):
                Recherche = Query()
                existing_player = table.get(
                    (Recherche.name == player._name) &
                    (Recherche.surname == player._surname) &
                    (Recherche.id_chess == player.id_chess)
                )
                if existing_player:
                    print(f"ERROR: {player._name} {player._surname} existe déjà dans le fichier{filename}.")
                else:
                    # Aucun joueur avec les mêmes informations, vous pouvez ajouter le nouveau joueur
                    table.insert(player.dictionnary_player())
                    print(f"SAVE: {player._name} {player._surname} dans la base de données.")
        db.close()

    def save_tournament_info_to_json(self, filename='./tournoi/players.json'):
        directory=os.path.dirname(filename)
        if not os.path.exists(directory):
            os.makedirs(directory)
        db = TinyDB(filename)
        table_name="save_info"
        if table_name in db.tables():
            db.drop_table(table_name)
            table=db.table("save_info")
            table.insert(self.dictionnary_tournament())
        db.close()

    def dictionnary_tournament(self):
        return {"name": self.name, "place": self.place, "date_start": self.date_start,"date_end": self.date_end,
                "actual_round": self.actual_round, "number_round":self.numbers_round}

    def rebuild_class(cls,filename='./tournoi/players.json'):
        pass

    @staticmethod
    def from_tinydb( filename='./tournoi/players.json'):
        db = TinyDB(filename)
        tournement_data = db.table("save_info").get(doc_id=1)
        if tournement_data:
            return Tournament(
                tournement_data['name'],
                tournement_data['place'],
                tournement_data['date_start'],
                tournement_data['date_end'],
                tournement_data['number_round']
            )
        else:
            return None



