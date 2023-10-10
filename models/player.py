from datetime import date


class Player:
    def __init__(self, name, surname, birthday, score, id_chess="AB12345"):
        self._name = name
        self._surname = surname
        self._birthday = birthday
        self.id_chess = id_chess
        self.score = score

    def __str__(self):
        return f"Nom:{self._name} Prenom:{self._surname} Naissance:{self._birthday} Score:{self.score} ID:{self.id_chess}"

    def __eq__(self, other):
        return self._name == other._name and self._surname == other._surname

    def dictionnary_player(self):
        return {"name": self._name, "surname": self._surname, "birtday": self._birthday.isoformat(),
                "score": self.score,
                "id_chess": self.id_chess}


if __name__ == "__main__":
    player1 = Player("Dupont", "Adrien", date(1990, 5, 15), 50)
    player2 = Player("Moline", "Séverine", date(1992, 2, 1), 500)
    player3 = Player("Kagon", "Nino", date(1988, 11, 4), 350)
    player4 = Player("Guyot", "Maxime", date(1998, 3, 27), 400)
    player5 = Player("Dalco", "Lucien", date(1995, 8, 12), 500)
    player6 = Player("Vardie", "Jennifer", date(1995, 7, 21), 275)
    player7 = Player("Dupont", "Adrien", date(1990, 5, 15), 50)

    if (player1==player7):
        print(True)
    else:
        print(False)
