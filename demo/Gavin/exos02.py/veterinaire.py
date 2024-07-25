from datetime import date, timedelta
from chien import Chien
from chat import Chat
from cheval import Cheval
from oiseau import Oiseau
class Veterinaire:
    def __init__(self):
        self.animaux = []
        self.jour_actuel = date.today()

    def ajouter_animal(self, type_animal, nom):
        if type_animal.lower() == "chien":
            animal = Chien(nom)
        elif type_animal.lower() == "chat":
            animal = Chat(nom)
        elif type_animal.lower() == "cheval":
            animal = Cheval(nom)
        elif type_animal.lower() == "oiseau":
            animal = Oiseau(nom)
        else:
            print("Type d'animal non reconnu.")
            return
        self.animaux.append(animal)
        print(f"{nom} ({type_animal}) a été ajouté.")

    def retirer_animal(self, nom):
        for animal in self.animaux:
            if animal.nom == nom:
                self.animaux.remove(animal)
                print(f"{nom} a été retiré.")
                return
        print(f"Aucun animal nommé {nom} n'a été trouvé.")

    def passer_jour_suivant(self):
        self.jour_actuel += timedelta(days=1)
        print(f"Nouveau jour : {self.jour_actuel}")
        for animal in self.animaux:
            animal.verifier_traitement(self.jour_actuel)
            animal.laver(self.jour_actuel)

    def menu(self):
        while True:
            print("1. Ajouter un animal")
            print("2. Retirer un animal")
            print("3. Passer au jour suivant")
            print("4. Quitter")
            choix = input("Choisissez une option : ")

            if choix == "1":
                type_animal = input("Type d'animal (chien/chat/cheval/oiseau) : ")
                nom = input("Nom de l'animal : ")
                self.ajouter_animal(type_animal, nom)
            elif choix == "2":
                nom = input("Nom de l'animal à retirer : ")
                self.retirer_animal(nom)
            elif choix == "3":
                self.passer_jour_suivant()
            elif choix == "4":
                break
            else:
                print("Option non valide.")

if __name__ == "__main__":
    veterinaire = Veterinaire()
    veterinaire.menu()