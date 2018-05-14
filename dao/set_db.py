from dao import *
from extensions import mongo

'''
-------------------------------
Instanciation des départements
-------------------------------
'''

tc = Departement(nom = "TC")
tc.insert()

bs = Departement(nom = "BS")
bs.insert()

ifo = Departement(nom = "IF")
ifo.insert()

'''
-------------------------------
-------------------------------
'''
