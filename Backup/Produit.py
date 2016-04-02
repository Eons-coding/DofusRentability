from Prix import Prix as ImportPrix


class Produit(ImportPrix):
    """
    Les ingredients composant une recette de craft. On represente ici leur prix, historique de prix et nom
    """

    def __init__(self, nom, price):
        self.nom = nom
        self.prix = ImportPrix(price)
        self.historique = []

    def ajoutPrix(self, nouveauPrix):
        self.appendHistorique()
        self.prix.cout = nouveauPrix
        self.prix.DateOfDay()


    def appendHistorique(self):
        self.historique.append(self.prix)