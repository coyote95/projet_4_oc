from tinydb import TinyDB, Query


class PlayerView:

    def view_player_bd(self, filename):
        db = TinyDB(filename)
        all_items = db.all()
        print(f"aperçu de la base de donnée {filename}:")
        for item in all_items:
            print(item)

    def display_player(self, player):
        print(f"Nom:{player.get_name()}\t"
              f"Prenom:{player.get_surname()}\t"
              f"Date de naissance:{player.get_birthday()}\t"
              f"ID_chess:{player.get_id_chess()}\t"
              )

    def input_name(self):
        print("Nom du joueur:")
        name = input(">>")
        return name.upper()

    def input_surname(self):
        print("Prenom du joueur:")
        surname = input(">>")
        return surname.upper()

    def input_birthday(self):
        while True:
            print("Date d'anniversaire: dd-mm-yyyy")
            birthday = input(">>")
            try:
                jour, mois, annee = map(int, birthday.split('-'))
                if 1 <= jour <= 31 and 1 <= mois <= 12 and 1900 <= annee:
                    return birthday
                else:
                    print(
                        "La date saisie est invalide")
            except ValueError:
                print("Format invalide. Assurez-vous de séparer la date par des tirets  (dd-mm-yyyy).")

    def input_id(self):
        print("Numero ID:")
        numero_id = input(">>")
        return numero_id.upper()
