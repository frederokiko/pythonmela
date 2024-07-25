from animal import Animal
class Chien(Animal):
    def verifier_traitement(self, jour_actuel):
        if (jour_actuel - self.derniere_verification).days >= 7:
            print(f"{self.nom} (chien) a reçu un traitement antipuce.")
            self.derniere_verification = jour_actuel