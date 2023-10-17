class PlayerController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def save_player_controller(self, filename):
        self.model.save_player_to_json(filename)

    def display_db(self,filename):
        self.view.view_player_bd(filename)

    def display_player_controller(self):
        self.view.display_player(self.model)

    def creation_player(self):
        print("Nom du joueur:")
        name = input(">>")
        self.model.new_name(name)
        print("Prenom du joueur:")
        surname = input(">>")
        self.model.new_surname(surname)
        print("Date d'anniversaire:")
        birthday = input(">>")
        self.model.new_birthday(birthday)
        print("Numero ID:")
        identie = input(">>")
        self.model.new_id(identie)






