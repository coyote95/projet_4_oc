class Round:
    def __init__(self, numero_round):
        self.numero_round = numero_round
        self.matchs = []

    def __str__(self):
        return (
            f"Numero du round: {self.numero_round} "
            f"matchs: {self.matchs}"
        )

    def add_match(self, match):
        self.matchs.append(match)




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

