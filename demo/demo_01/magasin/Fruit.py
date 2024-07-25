from Article import Article
class Fruit(Article):
    def __init__(self, nom, quantite, prix):
        super().__init__(nom, quantite, prix)
        self.type = 'Fruit'