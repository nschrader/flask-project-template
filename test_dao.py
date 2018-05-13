from dao import *

#TODO: Find a better place to put test code
tc = Departement(nom = "TC")
tc.insert()
print(tc.__dict__)

bs = Departement(nom = "BS")
bs.insert()
print(bs.__dict__)

corentin = Utilisateur(prenom = "Corentin", nom = "Leroy", departement = tc._id,
niveau = 3, mobilite = False, mail = "corentin.leroy@insa-lyon.fr")
print(corentin.__dict__)
corentin.insert()

coco = Utilisateur.get(str(corentin._id))
print(coco.__dict__)

corentin.update(departement=bs._id)
print(corentin.__dict__)

suede = Pays(nom = "Suède", continent = "Europe", climat = "climat",
culture = "culture", vie_pratique = "vie_pratique", tourisme = "tourisme")
print(suede.__dict__)
suede.insert()

kth = Universite(nom = "KTH", pays = "Suède", departements = [tc._id, bs._id])
print(kth.__dict__)
kth.insert()

suede.universites = [kth._id]
suede.update()
print(suede.__dict__)

bs.remove()
print(Departement.get_all())
print(Departement.get(str(bs._id)))

lummerland = Pays(nom = "lummerland")
lummerland.remove()
