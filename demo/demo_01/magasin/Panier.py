from Poire import Poire
from Pomme import Pomme
from Steack import Steack
from Entrecote import Entrecote

class Panier:
    def __init__(self):
        self.articles = []

    def ajouter_article(self, article, quantite):
        if article.diminuer_quantite(quantite):
            self.articles.append((article, quantite))
            print(f"{quantite} {article.nom}(s) ajouté(s) au panier.")

    def retirer_article(self, nom_article):
        for article, quantite in self.articles:
            if article.nom == nom_article:
                self.articles.remove((article, quantite))
                print(f"{article.nom} retiré du panier.")
                return
        print(f"{nom_article} n'est pas dans le panier.")

    def afficher_panier(self):
        if not self.articles:
            print("Le panier est vide.")
            return
        print("Contenu du panier :")
        for article, quantite in self.articles:
            print(f"Nom: {article.nom}, Quantité: {quantite}, Prix: {article.prix:.2f}, Type: {article.type}")

    def calculer_total(self):
        total = sum(article.prix * quantite for article, quantite in self.articles)
        return total

    def afficher_recapitulatif(self):
        self.afficher_panier()
        print(f"Total du panier: {self.calculer_total():.2f} €")

poire1 = Poire(10, 2.20)
pomme1 = Pomme(10, 1.5)
steak1 = Steack(10, 3.5)
entrecote1 = Entrecote(10, 3.5)
articles_disponibles = [poire1, pomme1, steak1, entrecote1]

def afficher_articles_disponibles():
    print("Articles disponibles :")
    for idx, article in enumerate(articles_disponibles, start=1):
        print(f"{idx}. Nom: {article.nom}, Quantité: {article.quantite}, Prix: {article.prix:.2f}, Type: {article.type}")
    print()
mon_panier = Panier()
while True:
    afficher_articles_disponibles()
    choix = input("Entrez le numéro de l'article à ajouter au panier (ou 'q' pour terminer) : ")
    if choix.lower() == 'q':
        break
    try:
        choix_num = int(choix) - 1
        if 0 <= choix_num < len(articles_disponibles):
            article_selectionne = articles_disponibles[choix_num]
            quantite = int(input(f"Entrez la quantité de {article_selectionne.nom} à ajouter au panier: "))
            mon_panier.ajouter_article(article_selectionne, quantite)
        else:
            print("Numéro invalide. Veuillez essayer à nouveau.")
    except ValueError:
        print("Entrée invalide. Veuillez entrer un numéro.")
print("\nVotre ticket de caisse :")
mon_panier.afficher_recapitulatif()
