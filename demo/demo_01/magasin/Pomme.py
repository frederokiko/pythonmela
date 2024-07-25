from Fruit import Fruit
class Pomme(Fruit):
    def __init__(self, quantite, prix):
        super().__init__('Pomme', quantite, prix)