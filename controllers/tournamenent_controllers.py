class TournamentController:

    def __init__(self, model, view):
        self.model = model
        self.view = view

    def display_player_tournament_controler(self):
        print("Liste des participants au tournoi:")
        self.view.display_players_tournament()

    def add_tournament_player_controller(self, player):
        self.model.add_tournament_player(player)

    def creation_tournoi(self):
        print("Nom du tournoi:")
        name = input(">>")
        self.model.new_name(name)
        print("lieu du tournoi:")
        place = input(">>")
        self.model.new_place(place)
        print("Date de debut du tournoi(aaaa,mm,jj):")
        start_date = input(">>")
        self.model.new_date_start(start_date)
        print("Date de fin du tournoi(aaaa,mm,jj):")
        end_date = input(">>")
        self.model.new_date_end(end_date)
        print("Nombre de round:")
        numbers_date = input(">>")
        self.model.new_numbers_round(numbers_date)




