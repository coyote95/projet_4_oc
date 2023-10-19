from tinydb import TinyDB, Query


class PlayerView:

    def view_player_bd(self,filename):
        db = TinyDB(filename)
        all_items = db.all()
        print (f"aperçu de la base de donnée {filename}:")
        for item in all_items:
            print(item)

    def display_player(self,player):
        print (f"Nom:{player.get_name()}\t"
               f"Prenom:{player.get_surname()}\t"
               f"Date de naissance:{player.get_birthday()}\t"
               f"ID_chess:{player.get_id_chess()}\t"
               )

    def input_name(self):
        print("Nom du joueur:")
        name = input(">>")
        return name

    def input_surname(self):
        print("Prenom du joueur:")
        surname = input(">>")
        return surname

    def input_birthday(self):
        print("Date d'anniversaire:")
        birthday = input(">>")
        return birthday

    def input_id(self):
        print("Numero ID:")
        numero_id = input(">>")
        return numero_id


        # while True:
        #     try:
        #         numero_id = input(">>")
        #         entier = int(numero_id)
        #         print(f"Vous avez entré un entier : {entier}")
        #         break
        #     except ValueError:
        #         print("L'entrée n'est pas un entier.")
        # return numero_id
