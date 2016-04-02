import lib_Craft as Dofus

testCraft = Dofus.Recettes("Alchimiste")
testCraft.cahier = []
testStock = Dofus.HotelDeVente()
testStock.ajout_ressource("Pics de Prespic", 200)
testStock.ajout_ressource("Kanigrou", 90)
testStock.ajout_ressource("Os de Chafer", 9)
testStock.ajout_ressource("Ortie", 0)
testStock.ajout_ressource("Blé", 2)
testCraft.ajout_craft("Potion de Bibliotemple", 210)
testCraft.cahier[0].add_ingredient(1, 1)
testCraft.cahier[0].add_ingredient(2, 1)
testCraft.ajout_craft("Potion de soin", 50)
testCraft.cahier[1].add_ingredient(3, 4)
testCraft.ajout_craft("Teinture Rougeatre Magique", 3000)
testCraft.cahier[2].add_ingredient(0, 3)
testCraft.cahier[2].add_ingredient(4, 2)
testCraft.cahier[0].add_ingredient(1, 1)


testCraft.cahier[0].calcul_rentability(testStock)
print("Rentabilité:", testCraft.cahier[0].rentability)
print("Date prix", testStock.ressources[1].nom, ":", testStock.ressources[1].cout, "le", testStock.ressources[1].date.valeur)

Dofus.save(testStock, "stock.dr")
Dofus.save(testCraft, "craft.dr")