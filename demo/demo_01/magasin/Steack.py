from Viande import Viande
class Steack(Viande):
    def __init__(self, quantite, prix):
        super().__init__('Steack', quantite, prix)