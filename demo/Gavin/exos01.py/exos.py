from datetime import datetime, timedelta

class Animal:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.last_antipuce_treatment = datetime.now()
        self.last_box_cleaning = datetime.now()
        self.last_wing_clipping = datetime.now()
        self.last_bathing = datetime.now()

    def __str__(self):
        return f"{self.type} nommé {self.name}"

class Veterinarian:
    def __init__(self):
        self.animals = []
        self.current_date = datetime.now()

    def add_animal(self, name, type):
        self.animals.append(Animal(name, type))
        print(f"{type} nommé {name} ajouté.")

    def remove_animal(self, name):
        self.animals = [animal for animal in self.animals if animal.name != name]
        print(f"Animal nommé {name} retiré.")

    def next_day(self):
        self.current_date += timedelta(days=1)
        print(f"Passage au jour suivant: {self.current_date.strftime('%Y-%m-%d')}")
        self.check_actions()

    def check_actions(self):
        for animal in self.animals:
            if animal.type in ["chien", "chat"]:
                if self.current_date - animal.last_antipuce_treatment >= timedelta(days=15):
                    print(f"Traitement antipuce pour {animal}.")
                    animal.last_antipuce_treatment = self.current_date
            if animal.type == "cheval":
                if self.current_date - animal.last_box_cleaning >= timedelta(days=7):
                    print(f"Nettoyage du box pour {animal}.")
                    animal.last_box_cleaning = self.current_date
            if animal.type == "oiseau":
                if self.current_date - animal.last_wing_clipping >= timedelta(days=20):
                    print(f"Coupe des ailes pour {animal}.")
                    animal.last_wing_clipping = self.current_date
            if self.current_date - animal.last_bathing >= timedelta(days=30):
                print(f"Bain pour {animal}.")
                animal.last_bathing = self.current_date

if __name__ == "__main__":
    vet = Veterinarian()

    while True:
        print("\nMenu:")
        print("1. Ajouter un animal")
        print("2. Retirer un animal")
        print("3. Passer au jour suivant")
        print("4. Quitter")

        choice = input("Entrez votre choix: ")

        if choice == "1":
            name = input("Entrez le nom de l'animal: ")
            type = input("Entrez le type de l'animal (chien, chat, cheval, oiseau): ").lower()
            if type in ["chien", "chat", "cheval", "oiseau"]:
                vet.add_animal(name, type)
            else:
                print("Type d'animal invalide.")
        elif choice == "2":
            name = input("Entrez le nom de l'animal à retirer: ")
            vet.remove_animal(name)
        elif choice == "3":
            vet.next_day()
        elif choice == "4":
            break
        else:
            print("Choix invalide.")
