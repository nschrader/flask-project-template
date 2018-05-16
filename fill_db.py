from dao import Utilisateur, Departement, Universite, Pays, Continent, Accord

tc = Departement(nom = "TC").insert()._id
pc = Departement(nom = "PC").insert()._id
gcu = Departement(nom = "GCU").insert()._id
ge = Departement(nom = "GE").insert()._id
gen = Departement(nom = "GEN").insert()._id
gi = Departement(nom = "GI").insert()._id
gm = Departement(nom = "GM").insert()._id
yf = Departement(nom = "IF").insert()._id
sgm = Departement(nom = "SGM").insert()._id

eu = Continent(nom = "Europe").insert()._id
na = Continent(nom = "Amérique du Nord").insert()._id
af = Continent(nom = "Afrique").insert()._id

de = Pays(nom = "Allemagne", climat="Froid", culture="strict", continent=eu,
vie_pratique="Bouteilles consignées", tourisme="Industriel").insert()._id
fi = Pays(nom = "Finlande", climat="Très froid", culture="froid", continent=eu,
vie_pratique="L'alcool est très cher", tourisme="Nature").insert()._id
ir = Pays(nom = "Irlande", climat="Pluie", culture="Bourée", continent=eu,
vie_pratique="Tout le monde est roux", tourisme="Partout").insert()._id
ca = Pays(nom = "Canada", climat="Froid", culture="Poutine", continent=na,
vie_pratique="On ne comprend personne", tourisme="West Coast").insert()._id
us = Pays(nom = "USA", climat="Moderé", culture="Red Neck", continent=na,
vie_pratique="Tout est gigantesque", tourisme="Parcs nationaux").insert()._id
bf = Pays(nom = "Bourkina Faso", climat="Chaud", culture="Mossi", continent=af,
vie_pratique="Il faut boire beacoup", tourisme="Safari").insert()._id

rwth = Universite(nom = "RWTH", infos="Se trouve à Aachen", pays=de,
accords=[Accord(type="Erasmus+", departements=["TC", "GE", "GM"]).insert()._id]).insert()._id
tu_b = Universite(nom = "Technische Universität Berlin", pays=de,
accords=[Accord(type="Erasmus+", departements=["TC", "GE", "GM"]).insert()._id]).insert()._id
kit = Universite(nom = "KIT", infos="Se trouve à Karlsruhe", pays=de,
accords=[Accord(type="Erasmus+", departements=["TC", "GE", "GM"]).insert()._id,
Accord(type="Double Diplôme", departements=["GM"]).insert()._id]).insert()._id
aalto = Universite(nom = "Aalto University", pays=fi,
accords=["Erasmus+"]).insert()._id
uh = Universite(nom = "University of Helsinki", pays=fi,
accords=["Erasmus+"]).insert()._id
uj = Universite(nom = "University of Jyväskylä", pays=fi,
accords=["Erasmus+"]).insert()._id
dcu = Universite(nom = "Dublin City Universiy", pays=ir,
accords=["Erasmus+"]).insert()._id
tcd = Universite(nom = "Trinity College – Dublin", pays=ir,
accords=["Erasmus+"]).insert()._id
ucd = Universite(nom = "University College of Dublin", pays=ir,
accords=["Erasmus+"]).insert()._id
epm = Universite(nom = "Ecole Polytechnique de Montréal", pays=ca,
accords=["Bilatéral"]).insert()._id
ets = Universite(nom = "École de Technologie Supérieure", pays=ca,
accords=["Bilatéral"]).insert()._id
iit = Universite(nom = "Illinois Institute of Technology", pays=us,
accords=["Bilatéral"], infos="Payant. Se trouve à Chicago").insert()._id
git = Universite(nom = "Georgia Institute of Technology", pays=us,
accords=["Bilatéral"], infos="Payant. Se trouve à Atlanta").insert()._id
iie = Universite(nom = "Institut International d’Ingénierie de l’Eau et de l’Environnement",
pays=bf, accords=["Bilatéral"], infos="Se trouve à Ouagadougou").insert()._id
