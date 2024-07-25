from animal import Animal
class Chat(Animal):
    def verifier_traitement(self, jour_actuel):
        if (jour_actuel - self.derniere_verification).days >= 7:
            print(f"{self.nom} (chat) a reçu un traitement antipuce.")
            self.derniere_verification = jour_actuel