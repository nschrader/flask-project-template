from dao import *
import extensions

StdUserProxy.set(Utilisateur.get_root())

tc = Departement(nom="TC").saveAndGet()
pc = Departement(nom="PC").saveAndGet()
gcu = Departement(nom="GCU").saveAndGet()
ge = Departement(nom="GE").saveAndGet()
gen = Departement(nom="GEN").saveAndGet()
gi = Departement(nom="GI").saveAndGet()
gm = Departement(nom="GM").saveAndGet()
yf = Departement(nom="IF").saveAndGet()
sgm = Departement(nom="SGM").saveAndGet()
bio = Departement(nom="BB/BIM").saveAndGet()
tous = Departement.objects.all()
#[tc, pc, gcu, ge, gen, gi, gm, yf, sgm, bio]

eu = Continent(nom="Europe").saveAndGet()
na = Continent(nom="Amérique du Nord").saveAndGet()
sa = Continent(nom="Amérique du Sud").saveAndGet()
af = Continent(nom="Afrique").saveAndGet()
ai = Continent(nom="Asie").saveAndGet()

ersms = Accord(nom="Erasmus+").saveAndGet()
dd = Accord(nom="Double Diplôme").saveAndGet()
untch = Accord(nom="UNITECH").saveAndGet()
spet = Accord(nom="SPE-T").saveAndGet()
mxftc = Accord(nom="MEXFITEC").saveAndGet()
brftc = Accord(nom="BRAFITEC").saveAndGet()
arftc = Accord(nom="ARFITEC").saveAndGet()

de = Pays(
    nom="Allemagne",
    climat=Article(text="Froid"),
    culture=Article(text="strict"),
    vie_pratique=Article(text="Bouteilles consignées"),
    tourisme=Article(text="Industriel"),
    continent=eu
).saveAndGet()
fi = Pays(
    nom="Finlande",
    climat=Article(text="Très froid"),
    culture=Article(text="froid"),
    vie_pratique=Article(text="L'alcool est très cher"),
    tourisme=Article(text="Nature"),
    continent=eu
).saveAndGet()
ir = Pays(
    nom="Irlande",
    climat=Article(text="Pluie"),
    culture=Article(text="Bourée"),
    vie_pratique=Article(text="Tout le monde est roux"),
    tourisme=Article(text="Partout"),
    continent=eu
).saveAndGet()
ca = Pays(
    nom="Canada",
    climat=Article(text="Froid"),
    culture=Article(text="Poutine"),
    vie_pratique=Article(text="On ne comprend personne"),
    tourisme=Article(text="West Coast"),
    continent=na
).saveAndGet()
us = Pays(
    nom="USA",
    climat=Article(text="Moderé"),
    culture=Article(text="Red Neck"),
    vie_pratique=Article(text="Tout est gigantesque"),
    tourisme=Article(text="Parcs nationaux"),
    continent=na
).saveAndGet()
bf = Pays(
    nom="Bourkina Faso",
    climat=Article(text="Chaud"),
    culture=Article(text="Mossi"),
    vie_pratique=Article(text="Il faut boire beacoup"),
    tourisme=Article(text="Safari"),
    continent=af
).saveAndGet()
ar = Pays(
    nom="Argentine",
    climat=Article(text="Caramba"),
    culture=Article(text="Hispanophone"),
    vie_pratique=Article(text="Mate partout"),
    tourisme=Article(text="Patagonie"),
    continent=sa
).saveAndGet()
br = Pays(
    nom="Brésil",
    climat=Article(text="Tropique"),
    culture=Article(text="Lusohone"),
    tourisme=Article(text="Les îles"),
    continent=sa
).saveAndGet()
mex = Pays(
    nom="Méxique",
    continent=sa
).saveAndGet()
hk = Pays(
    nom="Hong Kong",
    climat=Article(text="Humide"),
    culture=Article(text="Anglais"),
    vie_pratique=Article(text="Il faut quand même parler chinois"),
    tourisme=Article(text="La ville"),
    continent=ai
).saveAndGet()
ch = Pays(
    nom="Chine",
    continent=ai
).saveAndGet()

rwth = Universite(
    nom="RWTH",
    infos=Article(text="Se trouve à Aachen"),
    pays=de,
    echanges=[
        Echange(accord=ersms, departements=[tc], places="5x4"),
        Echange(accord=ersms, departements=[ge, gm], places="12x1"),
        Echange(accord=untch, departements=tous, places="12x2"),
    ]
).saveAndGet()
tu_b = Universite(
    nom="Technische Universität Berlin",
    pays=de,
    echanges=[
        Echange(accord=ersms, departements=[tc, ge], places="8x5"),
        Echange(accord=ersms, departements=[gm], places="12x1"),
    ]
).saveAndGet()
kit = Universite(
    nom="KIT",
    infos=Article(text="Se trouve à Karlsruhe"),
    pays=de,
    echanges=[
        Echange(accord=ersms, departements=[tc, ge, gm], places="3x10"),
        Echange(accord=dd, departements=[gm], places="3x4")
    ]
).saveAndGet()
aalto = Universite(
    nom="Aalto University",
    pays=fi,
    echanges=[
        Echange(accord=ersms, departements=[bio, sgm, pc], places="6x4")
    ]
).saveAndGet()
uh = Universite(
    nom="University of Helsinki",
    pays=fi,
    echanges=[
        Echange(accord=ersms, departements=[bio, ge, pc], places="12x4")
    ]
).saveAndGet()
uj = Universite(
    nom="University of Jyväskylä",
    pays=fi,
    echanges=[
        Echange(accord=ersms, departements=[bio, sgm, pc], places="6x10")
    ]
).saveAndGet()
dcu = Universite(
    nom="Dublin City Universiy",
    pays=ir,
    echanges=[
        Echange(accord=ersms, departements=tous, places="3x6")
    ]
).saveAndGet()
tcd = Universite(
    nom="Trinity College – Dublin",
    pays=ir,
    echanges=[
        Echange(accord=ersms, departements=[gi, tc], places="8x4"),
        Echange(accord=dd, departements=[gm], places="12x3"),
        Echange(accord="UNITECH", departements=[yf], places="12x1")
    ]
).saveAndGet()
ucd = Universite(
    nom="University College of Dublin",
    pays=ir,
    echanges=[
        Echange(accord=ersms, departements=[yf, sgm], places="6x3")
    ]
).saveAndGet()
epm = Universite(
    nom="Ecole Polytechnique de Montréal",
    pays=ca,
    echanges=[
        Echange(accord="Bilatéral", departements=[gcu, sgm], places="12x2")
    ]
).saveAndGet()
ets = Universite(
    nom="École de Technologie Supérieure",
    pays=ca,
    echanges=[
        Echange(accord="Bilatéral", departements=[bio], places="6x6")
    ]
).saveAndGet()
iit = Universite(
    nom="Illinois Institute of Technology",
    pays=us,
    echanges=[
        Echange(accord="Bilatéral", departements=[gm], places="12x2"),
        Echange(accord="Bilatéral", departements=[gm, ge, gi], places="12x1")
    ]
).saveAndGet()
git = Universite(
    nom="Georgia Institute of Technology",
    pays=us,
    echanges=[
        Echange(accord="Bilatéral", departements=[yf], places="5x4"),
        Echange(accord=dd, departements=[ge, gm, sgm, yf, tc], places="6x6"),
    ],
    infos=Article(text="Payant. Se trouve à Atlanta")
).saveAndGet()
iie = Universite(
    nom="Institut International d’Ingénierie de l’Eau et de l’Environnement",
    pays=bf,
    echanges=[
        Echange(accord="Bilatéral", departements=tous, places="12x2")
    ],
    infos=Article(text="Se trouve à Ouagadougou")
).saveAndGet()
ul = Universite(
    nom="Université Laval",
    pays=ca,
    echanges=[
        Echange(accord="BCI", departements=[ge, gi], places="6x4")
        ],
    infos=Article(text="Se trouve à Québec")
).saveAndGet()
ush = Universite(
    nom="Université de Sherbrooke",
    pays=ca,
    echanges=[
        Echange(accord="BCI", departements=[yf], places="6x2")
    ]
).saveAndGet()
ryu = Universite(
    nom="Ryerson University",
    pays=ca,
    echanges=[
        Echange(accord="ORA", departements=[gcu, sgm], places="12x1")
    ]
).saveAndGet()
udp = Universite(
    nom="Universidad de Palermo",
    pays=ar,
    echanges=[
        Echange(accord="ISEP", departements=[gm], places="6x6")
    ],
    infos=Article(text="Se trouve à Buenos Aires")
).saveAndGet()
hkpu = Universite(
    nom="Hong Kong Polytechnic University",
    pays=hk,
    echanges=[
        Echange(accord="Global E3", departements=[gm], places="3x6")
    ]
).saveAndGet()
ur = Universite(
    nom="Universidad de Rosario",
    pays=ar,
    echanges=[
        Echange(accord="ARFITEC", departements=[tc, pc, gm], places="6x2")
    ]
).saveAndGet()
unicamp = Universite(
    nom="Universidade Estadual de Campina",
    pays=br,
    echanges=[
        Echange(accord="BRAFITEC", departements=[bio], places="6x3")
    ]
).saveAndGet()
udg = Universite(
    nom="Universidad de Guadalajar",
    pays=mex,
    echanges=[
        Echange(accord="MEXFITEC", departements=[yf, ge], places="12x1")
    ]
).saveAndGet()
udg = Universite(
    nom="Shanghai Jiaotong University",
    pays=ch,
    echanges=[
        Echange(accord="SPE-T", departements=[tc], places="6x18")
    ]
).saveAndGet()
