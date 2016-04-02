from tkinter import *
from tkinter import tix

import lib_Craft as Dofus


craft = Dofus.Recettes
stock = Dofus.HotelDeVente

craft = Dofus.load("craft.dr")
stock = Dofus.load("stock.dr")


craft.cahier = sorted(craft.cahier, key=Dofus.tri('nom'))
craft.show_cahier()
fenetre = Tk()

def Affiche(evt):
    print (varcombo.get()) ## On affiche a l'ecran la valeur selectionnee

root = tix.Tk()
root.tk.eval('package require Tix')
varcombo = tix.StringVar()
combo = tix.ComboBox(root, editable=1, dropdown=1, variable=varcombo, command = Affiche)
combo.entry.config(state='readonly')  ## met la zone de texte en lecture seule
combo.insert(0, 'NT')
combo.insert(1, 'Linux')
combo.pack()
root.mainloop()

"""
cadre = Frame(fenetre, width=768, height=576, borderwidth=1)
cadre.pack(fill=BOTH)

message = Label(cadre, text="Notre fenêtre")
message.pack(side="bottom", fill=X)

# On démarre la boucle Tkinter qui s'interompt quand on ferme la fenêtre
fenetre.mainloop()
"""
