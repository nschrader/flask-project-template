import db
import utilisateur
import pays
import universite

corentin = utilisateur.Utilisateur(69, "Corentin", "Leroy", "TC", 3, False, "corentin.leroy@insa-lyon.fr")
print(corentin)
corentin.insererDansCollection()
coco = db.getUtilisateur(69)
print(coco)
corentin.update(departement='BS')
print(corentin)
suede = pays.Pays(12, "Suède", "Europe", "climat", "culture", "vie_pratique", "tourisme")
suede.insererDansCollection()
print(suede)
kth = universite.Universite(3, "KTH", "Suède", ["TC", "IF"])
print(kth)
kth.insererDansCollection()
suede.update()
print(suede)
