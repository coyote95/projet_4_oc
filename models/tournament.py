from tinydb import TinyDB, Query
from models.player import Player
from models.round import Round
import os


class Tournament:
    def __init__(self, name, place, date_start, date_end, numbers_round=4,
                 actual_round=0, list_players=None,
                 list_round=None):
        if list_players is None:
            list_players = []
        if list_round is None:
            list_round = []
        self.name = name
        self.place = place
        self.date_start = date_start
        self.date_end = date_end
        self.numbers_round = numbers_round
        self.actual_round = actual_round
        self.list_round = list_round
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

    def get_list_rounds(self):
        return self.list_round

    def get_numbers_round(self):
        return self.numbers_round

    def get_actual_round(self):
        return self.actual_round

    def get_name(self):
        return self.name

    def get_place(self):
        return self.place

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

    def set_round(self, game_round):
        self.numbers_round = game_round

    def nombre_de_participant_pair(self):
        if len(self.tournament_players) % 2 == 0:
            return True
        else:
            return False

    def nombre_de_participants(self):
        return len(self.tournament_players)

    def add_tournament_player(self, player):
        self.tournament_players.append(player)

    def add_list_tournament_round(self, game_round):
        self.list_round.append(game_round)

    def increment_actual_round(self):
        self.actual_round += 1

    def save_player_tournament_to_json(self, filename):
        list_player = []
        for player in self.tournament_players:
            if isinstance(player, Player):
                list_player.append(player.find_doc_id_player())

        directory = os.path.dirname(filename)
        if not os.path.exists(directory):
            os.makedirs(directory)
        db = TinyDB(filename)
        search = Query()
        result = db.search((search.name == self.name) &
                           (search.place == self.place))
        if result:
            doc_id = result[0].doc_id
            db.update({'list_doc_id_players': list_player},
                      doc_ids=[doc_id])
        else:
            print("ERROR: Le tournoi n'existe pas!")
        db.close()

    def save_tournament_info_to_json(self, filename):
        directory = os.path.dirname(filename)
        if not os.path.exists(directory):
            os.makedirs(directory)
        db = TinyDB(filename)
        search = Query()
        result = db.search((search.name == self.name) &
                           (search.place == self.place))
        if result:
            doc_id = result[0].doc_id
            db.update(self.dictionnary_tournament(), doc_ids=[doc_id])
        else:
            db.insert(self.dictionnary_tournament())
        db.close()

    def dictionnary_tournament(self):
        return {"name": self.name, "place": self.place,
                "date_start": self.date_start, "date_end": self.date_end,
                "actual_round": self.actual_round,
                "number_round": self.numbers_round,
                "list_doc_id_players": None, "list_doc_id_rounds": None}

    @staticmethod
    def from_tinydb(numero, filename='./tournoi/tournaments.json'):
        db = TinyDB(filename)
        tournement_data = db.get(doc_id=numero)
        if tournement_data:
            return Tournament(
                tournement_data['name'],
                tournement_data['place'],
                tournement_data['date_start'],
                tournement_data['date_end'],
                tournement_data['number_round'],
                tournement_data['actual_round'],
                Player.from_tinydb_list_player_tournement(
                    tournement_data["list_doc_id_players"]),
                Round.from_tinydb_list_round_tournement(
                    tournement_data["list_doc_id_rounds"])
            )
        else:
            return None

    @staticmethod
    def from_tinydb_all(filename='./tournoi/tournaments.json'):
        db = TinyDB(filename)
        doc_ids = db.all()
        list_tournaments = []
        for doc_id in doc_ids:
            new_tounrament = Tournament.from_tinydb(doc_id.doc_id, filename)
            new_tounrament.update_score_players()
            list_tournaments.append(new_tounrament)
        return list_tournaments

    def update_score_players(self):
        for round in self.list_round:
            for match in round.matchs:
                for players in self.tournament_players:
                    if match.player1 == players.name:
                        players.score += match.score1
                    if match.player2 == players.name:
                        players.score += match.score2

    def save_round_tournament_to_json(self, filename):
        list_round = []
        for game_round in self.list_round:
            if isinstance(game_round, Round):
                list_round.append(game_round.find_doc_id_round())
        directory = os.path.dirname(filename)
        if not os.path.exists(directory):
            os.makedirs(directory)
        db = TinyDB(filename)
        search = Query()
        result = db.search((search.name == self.name) &
                           (search.place == self.place))
        if result:
            doc_id = result[0].doc_id
            db.update({'list_doc_id_rounds': list_round},
                      doc_ids=[doc_id])
            db.update({'actual_round': self.actual_round},
                      doc_ids=[doc_id])
        else:
            print("ERROR: Le tournoi n'existe pas!")
        db.close()

    def sort_players_by_score(self):
        for personne in range(0, len(self.tournament_players)):
            self.set_tournament_players(sorted(self.tournament_players,
                                               key=lambda player: player.score,
                                               reverse=True))

    def get_remaining_players(self):
        remaining_players = [player for player in self.tournament_players]
        return remaining_players

    def remove_players(self, players_to_remove):
        for player in players_to_remove:
            if player in self.tournament_players:
                self.tournament_players.remove(player)
