from tinydb import TinyDB, Query
from models.player import Player
from models.round import Round
import os


class Tournament:
    def __init__(self, name, place, date_start, date_end, numbers_round=4, actual_round=1, list_players=[]):
        self.name = name
        self.place = place
        self.date_start = date_start
        self.date_end = date_end
        self.numbers_round = numbers_round
        self.actual_round = actual_round
        self.list_round = []
        self.tournament_players = list_players  # liste de dictionnaire
        self.description = []

    def __str__(self):
        return (
            f"*********Tournoi*******\n"
            f"Nom: {self.name} \n"
            f"Place: {self.place}\n"
            f"Date de debut: {self.date_start}\n"
            f"Date de fin: {self.date_end}\n"
            f"nombre de round: {self.numbers_round}\n"
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

    def get_actual_round(self):
        return self.actual_round

    def get_name(self):
        return self.name

    def set_tournament_players(self, list_players):
        self.tournament_players = list_players

    def set_name(self, name):
        self.name = name.upper()

    def set_place(self, place):
        self.place = place.upper()

    def set_date_start(self, date_start):
        self.date_start = date_start

    def set_date_end(self, date_end):
        self.date_end = date_end

    def set_round(self, round):
        self.numbers_round = round

    def nombre_de_participant_pair(self):
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

    def save_player_tournament_to_json(self, filename):
        directory = os.path.dirname(filename)
        if not os.path.exists(directory):
            os.makedirs(directory)
        db = TinyDB(filename)
        if table_name in db.tables():
            db.drop_table(table_name)
        db.close()
        for player in self.tournament_players:
            if isinstance(player, Player):
                player.save_player_to_json(filename, table_name, score=True)

    def save_tournament_info_to_json(self, filename):

        directory = os.path.dirname(filename)
        if not os.path.exists(directory):
            os.makedirs(directory)

        db = TinyDB(filename)
        Recherche = Query()
        result = db.search((Recherche.name == self.name) & (Recherche.place == self.place))
        if result:
            # Le `doc_id` du premier enregistrement correspondant (s'il y en a plusieurs) peut être obtenu comme suit :
            doc_id = result[0].doc_id
            db.update(self.dictionnary_tournament(),doc_ids=[doc_id])
            print(f"Le doc_id du championnat est {doc_id}")
        else:
            print(f"Aucun joueur avec le nom {self.name} = {Recherche.name} n'a été trouvé.")
            db.insert(self.dictionnary_tournament())
        db.close()

    def dictionnary_tournament(self):
        return {"name": self.name, "place": self.place, "date_start": self.date_start, "date_end": self.date_end,
                "actual_round": self.actual_round, "number_round": self.numbers_round,
                "actual_round": self.actual_round}

    @staticmethod
    def from_tinydb(filename='./tournoi/players.json'):
        db = TinyDB(filename)
        tournement_data = db.table("save_info").get(doc_id=1)
        if tournement_data:
            return Tournament(
                tournement_data['name'],
                tournement_data['place'],
                tournement_data['date_start'],
                tournement_data['date_end'],
                tournement_data['number_round'],
                tournement_data['actual_round'],
                Player.from_tinydb_all()
            )
        else:
            return None

    def save_round_tournament_to_json(self, filename, table_name):
        filename = './data/tournements/' + filename + ".json"
        directory = os.path.dirname(filename)
        if not os.path.exists(directory):
            os.makedirs(directory)
        db = TinyDB(filename)
        if table_name in db.tables():
            db.drop_table(table_name)
        table = db.table(table_name)
        for round_tournament in self.list_round:
            if isinstance(round_tournament, Round):
                table.insert(round_tournament.dictionnary_round())
                print(f"SAVE:{round_tournament}")

        db.close()

    def sort_players_by_score(self):
        for personne in range(0, len(self.tournament_players)):
            self.set_tournament_players(sorted(self.tournament_players,
                                               key=lambda player: player.score,
                                               reverse=True))
