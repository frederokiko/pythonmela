from animal import Animal
class Oiseau(Animal):
    def verifier_traitement(self, jour_actuel):
        if (jour_actuel - self.derniere_verification).days >= 15:
            print(f"Les ailes de {self.nom} (oiseau) ont été coupées.")
            self.derniere_verification = jour_actuel