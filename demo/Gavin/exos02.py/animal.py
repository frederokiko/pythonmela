from datetime import date, timedelta
class Animal:
    def __init__(self, nom):
        self.nom = nom
        self.date_arrivee = date.today()
        self.derniere_verification = self.date_arrivee
        self.dernier_bain = self.date_arrivee

    def verifier_traitement(self, jour_actuel):
        pass

    def laver(self, jour_actuel):
        if (jour_actuel - self.dernier_bain).days >= 30:
            print(f"{self.nom} a été lavé.")
            self.dernier_bain = jour_actuel