class HomeMenuView:
    def __init__(self, menu):
        self.menu = menu

    def _display_menu(self):
        for key, entry in self.menu.items():
            print(f"{key}: {entry.option}")

    @staticmethod
    def display_message_accueil():
        print()
        print("*******   ACCUEIL     *******")

    @staticmethod
    def display_message_continue(numero_round):
        print(f"Voulez vous jouer le round {numero_round} ?")

    @staticmethod
    def display_message_gagnant():
        print("Le gagnant est:")

    @staticmethod
    def display_message_liste_tournoi():
        print("*****  Liste de tous les tournois  ******")

    @staticmethod
    def display_message_list_players():
        print("*****  Liste de tous les Joueurs  ******")

    @staticmethod
    def display_message_end_programme():
        print("*****  Fin du programme  ******")

    @staticmethod
    def display_message_reprendre_tournoi():
        print("*****  Reprendre tournoi  ******")

    def get_user_choice(self):
        while True:
            # afficher le menu à l'utilisateur
            self._display_menu()
            # demander à l'utilisateur de faire un choix
            choice = input(">> ")
            # valider le choix de l'utilisateur
            if choice in self.menu:
                # retourner le choix de l'utilisateur
                return self.menu[choice]
