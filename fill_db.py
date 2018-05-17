from dao import Utilisateur, Departement, Universite, Pays, Continent, Accord, Article
import config

try:
    su = Utilisateur.make_root(config.ROOT, config.ROOT_PSWD)
except FileExistsError:
    su = Utilisateur.get_mail(config.ROOT)
finally:
    for entity in [Departement, Universite, Pays, Continent, Accord, Article]:
        entity.std_user = su._id

tc = Departement(nom="TC").insert()._id
pc = Departement(nom="PC").insert()._id
gcu = Departement(nom="GCU").insert()._id
ge = Departement(nom="GE").insert()._id
gen = Departement(nom="GEN").insert()._id
gi = Departement(nom="GI").insert()._id
gm = Departement(nom="GM").insert()._id
yf = Departement(nom="IF").insert()._id
sgm = Departement(nom="SGM").insert()._id
bio = Departement(nom="BB/BIM").insert()._id

eu = Continent(nom="Europe").insert()._id
na = Continent(nom="Amérique du Nord").insert()._id
sa = Continent(nom="Amérique du Sud").insert()._id
af = Continent(nom="Afrique").insert()._id
ai = Continent(nom="Asie").insert()._id

de = Pays(
    nom="Allemagne",
    climat=Article(text="Froid").insert()._id,
    culture=Article(text="strict").insert()._id,
    vie_pratique=Article(text="Bouteilles consignées").insert()._id,
    tourisme=Article(text="Industriel").insert()._id,
    continent=eu
).insert()._id
fi = Pays(
    nom="Finlande",
    climat=Article(text="Très froid").insert()._id,
    culture=Article(text="froid").insert()._id,
    vie_pratique=Article(text="L'alcool est très cher").insert()._id,
    tourisme=Article(text="Nature").insert()._id,
    continent=eu
).insert()._id
ir = Pays(
    nom="Irlande",
    climat=Article(text="Pluie").insert()._id,
    culture=Article(text="Bourée").insert()._id,
    vie_pratique=Article(text="Tout le monde est roux").insert()._id,
    tourisme=Article(text="Partout").insert()._id,
    continent=eu
).insert()._id
ca = Pays(
    nom="Canada",
    climat=Article(text="Froid").insert()._id,
    culture=Article(text="Poutine").insert()._id,
    vie_pratique=Article(text="On ne comprend personne").insert()._id,
    tourisme=Article(text="West Coast").insert()._id,
    continent=na
).insert()._id
us = Pays(
    nom="USA",
    climat=Article(text="Moderé").insert()._id,
    culture=Article(text="Red Neck").insert()._id,
    vie_pratique=Article(text="Tout est gigantesque").insert()._id,
    tourisme=Article(text="Parcs nationaux").insert()._id,
    continent=na
).insert()._id
bf = Pays(
    nom="Bourkina Faso",
    climat=Article(text="Chaud").insert()._id,
    culture=Article(text="Mossi").insert()._id,
    vie_pratique=Article(text="Il faut boire beacoup").insert()._id,
    tourisme=Article(text="Safari").insert()._id,
    continent=af
).insert()._id
ar = Pays(
    nom="Argentine",
    climat=Article(text="Caramba").insert()._id,
    culture=Article(text="Hispanophone").insert()._id,
    vie_pratique=Article(text="Mate partout").insert()._id,
    tourisme=Article(text="Patagonie").insert()._id,
    continent=sa
).insert()._id
br = Pays(
    nom="Brésil",
    climat=Article(text="Tropique").insert()._id,
    culture=Article(text="Lusohone").insert()._id,
    tourisme=Article(text="Les îles").insert()._id,
    continent=sa
).insert()._id
mex = Pays(
    nom="Méxique",
    continent=sa
).insert()._id
hk = Pays(
    nom="Hong Kong",
    climat=Article(text="Humide").insert()._id,
    culture=Article(text="Anglais").insert()._id,
    vie_pratique=Article(text="Il faut quand même parler chinois").insert()._id,
    tourisme=Article(text="La ville").insert()._id,
    continent=ai
).insert()._id
ch = Pays(
    nom="Chine",
    continent=ai
).insert()._id

rwth = Universite(
    nom="RWTH",
    infos=Article(text="Se trouve à Aachen").insert()._id,
    pays=de,
    accords=[
        Accord(type="Erasmus+", departements=[tc, ge, gm]).insert()._id,
        Accord(type="UNITECH", departements=[sgm]).insert()._id,
    ]
).insert()._id
tu_b = Universite(
    nom="Technische Universität Berlin",
    pays=de,
    accords=[Accord(type="Erasmus+", departements=[tc, ge, gm]).insert()._id]
).insert()._id
kit = Universite(
    nom="KIT",
    infos=Article(text="Se trouve à Karlsruhe").insert()._id,
    pays=de,
    accords=[
        Accord(type="Erasmus+", departements=[tc, ge, gm]).insert()._id,
        Accord(type="Double Diplôme", departements=[gm]).insert()._id
    ]
).insert()._id
aalto = Universite(
    nom="Aalto University",
    pays=fi,
    accords=[Accord(type="Erasmus+", departements=[bio, sgm, pc]).insert()._id]
).insert()._id
uh = Universite(
    nom="University of Helsinki",
    pays=fi,
    accords=[Accord(type="Erasmus+", departements=[bio, ge, pc]).insert()._id]
).insert()._id
uj = Universite(
    nom="University of Jyväskylä",
    pays=fi,
    accords=[Accord(type="Erasmus+", departements=[bio, sgm, pc]).insert()._id]
).insert()._id
dcu = Universite(
    nom="Dublin City Universiy",
    pays=ir,
    accords=[Accord(type="Erasmus+", departements=[yf, ge, gm]).insert()._id]
).insert()._id
tcd = Universite(
    nom="Trinity College – Dublin",
    pays=ir,
    accords=[
        Accord(type="Erasmus+", departements=[gi, tc]).insert()._id,
        Accord(type="Double Diplôme", departements=[gm]).insert()._id,
        Accord(type="UNITECH", departements=[yf]).insert()._id
    ]
).insert()._id
ucd = Universite(
    nom="University College of Dublin",
    pays=ir,
    accords=[Accord(type="Erasmus+", departements=[yf, sgm]).insert()._id]
).insert()._id
epm = Universite(
    nom="Ecole Polytechnique de Montréal",
    pays=ca,
    accords=[Accord(type="Bilatéral", departements=[gcu, sgm]).insert()._id]
).insert()._id
ets = Universite(
    nom="École de Technologie Supérieure",
    pays=ca,
    accords=[Accord(type="Bilatéral", departements=[bio]).insert()._id]
).insert()._id
iit = Universite(
    nom="Illinois Institute of Technology",
    pays=us,
    accords=[Accord(type="Bilatéral", departements=[gm, ge, gi]).insert()._id]
).insert()._id
git = Universite(
    nom="Georgia Institute of Technology",
    pays=us,
    accords=[
        Accord(type="Bilatéral", departements=[yf]).insert()._id,
        Accord(type="Double Diplôme", departements=[ge, gm, sgm, yf, tc]).insert()._id,
    ],
    infos=Article(text="Payant. Se trouve à Atlanta").insert()._id
).insert()._id
iie = Universite(
    nom="Institut International d’Ingénierie de l’Eau et de l’Environnement",
    pays=bf,
    accords=[Accord(type="Bilatéral", departements=[tc, ge, gm, gi, sgm, yf]).insert()._id],
    infos=Article(text="Se trouve à Ouagadougou").insert()._id
).insert()._id
ul = Universite(
    nom="Université Laval",
    pays=ca,
    accords=[Accord(type="BCI", departements=[ge, gi]).insert()._id],
    infos=Article(text="Se trouve à Québec").insert()._id
).insert()._id
ush = Universite(
    nom="Université de Sherbrooke",
    pays=ca,
    accords=[Accord(type="BCI", departements=[yf]).insert()._id]
).insert()._id
ryu = Universite(
    nom="Ryerson University",
    pays=ca,
    accords=[Accord(type="ORA", departements=[gcu, sgm]).insert()._id]
).insert()._id
udp = Universite(
    nom="Universidad de Palermo",
    pays=ar,
    accords=[Accord(type="ISEP", departements=[gm]).insert()._id],
    infos=Article(text="Se trouve à Buenos Aires").insert()._id
).insert()._id
hkpu = Universite(
    nom="Hong Kong Polytechnic University",
    pays=hk,
    accords=[Accord(type="Global E3", departements=[gm]).insert()._id]
).insert()._id
ur = Universite(
    nom="Universidad de Rosario",
    pays=ar,
    accords=[Accord(type="ARFITEC", departements=[tc, pc, gm]).insert()._id]
).insert()._id
unicamp = Universite(
    nom="Universidade Estadual de Campina",
    pays=br,
    accords=[Accord(type="BRAFITEC", departements=[bio]).insert()._id]
).insert()._id
udg = Universite(
    nom="Universidad de Guadalajar",
    pays=mex,
    accords=[Accord(type="MEXFITEC", departements=[yf, ge]).insert()._id]
).insert()._id
udg = Universite(
    nom="Shanghai Jiaotong University",
    pays=ch,
    accords=[Accord(type="SPE-T", departements=[tc]).insert()._id]
).insert()._id
