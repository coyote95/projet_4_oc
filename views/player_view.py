from tinydb import TinyDB


class PlayerView:

    @staticmethod
    def view_player_bd(filename):
        db = TinyDB(filename)
        all_items = db.all()
        print(f"aperçu de la base de donnée {filename}:")
        for item in all_items:
            print(item)

    @staticmethod
    def display_player(player):
        print(f"Nom:{player.get_name()}\t"
              f"Prenom:{player.get_surname()}\t"
              f"Date de naissance:{player.get_birthday()}\t"
              f"ID_chess:{player.get_id_chess()}\t"
              )

    @staticmethod
    def input_name():
        print("Nom du joueur:")
        name = input(">>")
        return name.upper()

    @staticmethod
    def input_surname():
        print("Prenom du joueur:")
        surname = input(">>")
        return surname.upper()

    @staticmethod
    def input_birthday():
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
                print("Format invalide. Assurez-vous de séparer la date par "
                      "des tirets  (dd-mm-yyyy).")

    @staticmethod
    def input_id():
        print("Numero ID:")
        numero_id = input(">>")
        return numero_id.upper()
