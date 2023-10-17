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

