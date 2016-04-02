import time
import pickle


def save(to_save, file_name):
    pickle.dump(to_save, open(file_name, "wb"))
    print("Saved")


def load(file_name):
    return pickle.load(open(file_name, "rb"))


class Date:
    def __init__(self):
        self.day = int(time.strftime('%d', time.localtime()))
        self.month = int(time.strftime('%m', time.localtime()))
        self.year = int(time.strftime('%y', time.localtime()))
        self.valeur = self.day + self.month * 100 + self.year * 10000


class Prix:
    """
    Le prix lié à la date.
    """

    def __init__(self, prix):
        self.cout = prix
        self.date = Date()

    def date_of_day(self):
        self.date = Date


class Produit(Prix):
    """
    Les ingredients composant une recette de craft. On represente ici leur prix, historique de prix et nom
    """

    def __init__(self, nom, price):
        super().__init__(price)
        self.nom = nom
        self.historique = []

    def ajout_prix(self, nouveau_prix):
        self.append_historique()
        self.prix.cout = nouveau_prix
        self.prix.date_of_day()

    def append_historique(self):
        self.historique.append(self.prix)


class Craft(Produit):
    """
    L'objet craft represente une recette de craft composée de max 8 ingredients.
    """
    nbIngredient = 8

    def __init__(self, name, price):
        """

        :rtype: Craft
        """
        super().__init__(name, price)
        self.ing_ID = []
        self.nb_ing = []
        self.rentability = 0
        self.historique = []

    def add_ingredient(self, id_stock, nb_ing):
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
            tampon += stock.ressources[self.ing_ID[i]].cout * self.nb_ing[i]

        self.rentability = self.cout - tampon
        print("Prix HDV:", self.cout, "-", tampon, "=", self.rentability)

    def afficher_ingredient(self, stock):
        for i in self.ing_ID[0:self.ing_ID]:
            print(stock[self.ing_ID[i]].nom, "-", stock[self.ing_ID[i]].prix.cout, "x", self.nb_ing[i])


def ajout_stock(stock_list, ns_nom, ns_prix):
    stock_list.append(Produit(ns_nom, ns_prix))


class Recettes():
    def __init__(self, metier):
        self.metier = metier
        self.cahier = []

    def ajout_craft(self, nc_nom, nc_prix):
        self.cahier.append(Craft(nc_nom, nc_prix))

    def retrait_craft(self, to_remove):
        self.cahier.remove(self.cahier[to_remove])

    def show_cahier(self):
        for i in self.cahier:
            print(i.nom, i.cout)


class HotelDeVente():
    def __init__(self):
        self.ressources = []

    def ajout_ressource(self, ns_nom, ns_prix):
        self.ressources.append(Produit(ns_nom, ns_prix))

    def retrait_ressource(self, to_remove):
        self.ressources.remove(self.ressources[to_remove])

    def show_ressources(self):
        for i in self.ressources[:]:
            print(i.nom, i.cout)


def tri(attr):
    def kicker(obj):
        return getattr(obj, attr)
    return kicker