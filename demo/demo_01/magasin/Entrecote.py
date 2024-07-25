from Viande import Viande
class Entrecote(Viande):
    def __init__(self, quantite, prix):
        super().__init__('Entrecote', quantite, prix)