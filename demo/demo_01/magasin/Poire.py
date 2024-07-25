from Fruit import Fruit
class Poire(Fruit):
    def __init__(self, quantite, prix):
        super().__init__('Poire', quantite, prix)