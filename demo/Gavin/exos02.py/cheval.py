from animal import Animal
class Cheval(Animal):
    def verifier_traitement(self, jour_actuel):
        if (jour_actuel - self.derniere_verification).days >= 20:
            print(f"Le box de {self.nom} (cheval) a été nettoyé.")
            self.derniere_verification = jour_actuel