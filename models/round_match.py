import random
from tinydb import TinyDB, Query

class Round:
    def __init__(self, numero_round=1):
        self.name="Round"
        self.numero_round = numero_round
        self.commence="date de debut"
        self.termine="date de fin"
        self.matchs = []

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

    def add_match(self, match):
        return self.matchs.append(match)

    def save_round_to_json(self, filename="save_round"):
        db = TinyDB(filename)
        db.insert(self.dictionnary_round())

    def dictionnary_round(self):
        return {"name": self.name, "numero_round": self.numero_round , "matchs": self.matchs}




class Match:
    def __init__(self,player1,score1,player2,score2):
        self.player1=player1
        self.player2=player2
        self.score1=score1
        self.score2=score2
        self.match=([player1,score1],[player2,score2])

    def __str__(self):
        return (
            f"Match: {self.player1} (score:{self.score1}) CONTRE {self.player2} (score: {self.score2})  "
        )

    def __repr__(self):
        return (
            f"Match: {self.player1} (score:{self.score1}) CONTRE {self.player2} (score: {self.score2})  "
        )



    def save_round_to_json(self, filename="save_match"):
        db = TinyDB(filename)
        db.insert(self.dictionnary_match())

    def dictionnary_match(self):
        return {"player1": self.player1.__dict__, "score1": self.score1, "player2": self.player2.__dict__, "score2": self.score2}

    def player1_gagnant(self):
        self.score1 += 1

    def player2_gagnant(self):
        self.score2 +=1

    def execo(self):
        self.score1 += 0.5
        self.score2 += 0.5

    def random_gagnant(self):
        choix_gagnant=random.choice([self.player1, self.player2,"execo"])
        if choix_gagnant == self.player1:
            self.score1 +=1
            print(f"le joueur gagant est:{choix_gagnant}")
           # self.player1_gagnant()

        elif choix_gagnant == self.player2:
            print(f"le joueur gagant est:{choix_gagnant}")
            self.player2_gagnant()
        elif choix_gagnant == "execo":
            print(f"Match nul!!")
            self.execo()
       # print( f"Nouveau score: {self.player1} (score:{self.score1}) CONTRE {self.player2} (score: {self.score2}) ")
        return choix_gagnant



