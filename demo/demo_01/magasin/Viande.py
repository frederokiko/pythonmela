from Article import Article
class Viande(Article):
    def __init__(self, nom, quantite, prix):
        super().__init__(nom, quantite, prix)
        self.type = 'Viande'