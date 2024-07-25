class Article:
    def __init__(self, nom, quantite, prix):
        self.nom = nom
        self.quantite = quantite
        self.prix = prix

    def diminuer_quantite(self, quantite):
        if quantite <= self.quantite:
            self.quantite -= quantite
            return True
        else:
            print(f"Pas assez de stock pour {self.nom}. Quantité disponible: {self.quantite}")
            return False
