class RoundMatchController:

    def __init__(self, model, view):
        self.model = model
        self.view = view

    def creation_round(self,tournament):
        round= tournament.get_numbers_round()
        for tour in range(round):
            print(f"round n° {tour}")





