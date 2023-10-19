from tinydb import TinyDB, Query

class Round:
    def __init__(self,list_math=[]):
        self.name="Round"
        self.numero_round = "1"
        self.commence="date de debut"
        self.termine="date de fin"
        self.matchs = list_math

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

    def __getitem__(self, choice): #Round[0]
        return self.matchs[choice]

    def get_match(self, match):
        return self.matchs

    def set_match(self, list):
        self.matchs=list

    def set_numero(self, num):
        self.numero_round=num

    def add_match(self, match):
        return self.matchs.append(match)

    def save_round_to_json(self, filename="save_round"):
        db = TinyDB(filename)
        db.insert(self.dictionnary_round())

    def dictionnary_round(self):
        return {"name": self.name, "numero_round": self.numero_round , "matchs": self.matchs}





