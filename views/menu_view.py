class HomeMenuView:
    def __init__(self, menu):
        self.menu = menu

    def _display_menu(self):
        """
        Display the menu options to the user.
        This method iterates through the menu items and prints the available options to the user,
         along with their corresponding keys.
        Returns:
            None
        """
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
        """
        Get the user's choice from the menu.
        This method displays the menu to the user, prompts them to make a choice,
        and validates the choice.
        Returns:
            callable or None: The selected menu option, which is a callable function,
             or None if the choice is invalid.
        """
        while True:
            self._display_menu()
            choice = input(">> ")
            if choice in self.menu:
                return self.menu[choice]
