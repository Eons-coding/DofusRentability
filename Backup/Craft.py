from Produit import Produit


class Craft(Produit):
    """
    L'objet craft represente une recette de craft composée de max 8 ingredients.
    """
    nbIngredient = 8

    def __init__(self, name, price):
        self.nom = name
        self.prixHDV = price
        self.ing_ID = []
        self.nb_ing = []
        self.rentability = 0
        self.historique = []

    def addIngredient(self, id_stock, id_ing, nb_ing):
        if len(self.ing_ID) <= 8:
            print("Ingredient", len(self.ing_ID), "ajouté")
            self.ing_ID.append(id_stock)
            self.nb_ing.append(nb_ing)
            return 1
        else:
            print("Cet objet a déjà assez d'ingredients ")
            return -1

    def nouveau_prix(self, prix):
        self.historique.append(self.prixHDV)
        # TODO ajout de la date dans le prix
        self.prixHDV = prix

    def calcul_rentability(self, stock):
        tampon = 0

        for i, val in enumerate(self.ing_ID):
            tampon += stock[self.ing_ID[i]].prix.cout * self.nb_ing[i]

        self.rentability = self.prixHDV - tampon
        print("Prix HDV:", self.prixHDV, "-", tampon, "=", self.rentability)

    def afficher_Ingredient(self, stock):
        for i in self.ing_ID[0:self.ing_ID]:
            print(stock[self.ing_ID[i]].nom, "-", stock[self.ing_ID[i]].prix.cout, "x", self.nb_ing[i])
