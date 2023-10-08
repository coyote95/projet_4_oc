import json
from datetime import date


class Player:
    def __init__(self, name, surname, birthday, score, id_chess="AB12345"):
        self.name = name
        self.surname = surname
        self.birthday = birthday
        self.id_chess = id_chess
        self.score = score

    def dictionnary_player(self):
        return {"name": self.name, "surname": self.surname, "birtday": self.birthday.isoformat(), "score": self.score,
                "id_chess": self.id_chess}

class NewPlayer:
    def __init__(self):
        self.players=[]

    def add_player(self,player):
        self.players.append(player)

    def _get_players(self):
        return self.players

    def save_to_json(self,filename):
        players_date=[player.dictionnary_player()for player in self.players] #modifier avec contain
        with open(filename,"w")as json_file:
            json.dump(players_date,json_file,indent=4)




if __name__ == "__main__":
    player1 = Player("Dupont", "Adrien", date(1990, 5, 15), 50)
    player2 = Player("Moline", "Séverine", date(1992, 2, 1), 500)
    player3 = Player("Kagon", "Nino", date(1988, 11, 4), 350)
    player4 = Player("Guyot", "Maxime", date(1998, 3, 27), 400)
    player5 = Player("Dalco", "Lucien", date(1995, 8, 12), 500)
    player6 = Player("Vardie", "Jennifer", date(1995, 7, 21), 275)
