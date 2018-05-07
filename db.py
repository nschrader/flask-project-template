import sys
import pymongo
from pprint import pprint
from bson.objectid import ObjectId
from utilisateur import Utilisateur
from pays import Pays
from universite import Universite

from pymongo import MongoClient
client = MongoClient('localhost', 27017)

# Base de données
db = client.database

# Collections
utilisateurs = db.utilisateurs
universites = db.universites
pays = db.pays

# Affiche tous les documents de la collection
def afficheCollection(collection) :
    tout = collection.find()
    for document in tout :
        pprint(document)

'''corentin = Utilisateur(69, "Corentin", "Leroy", "TC", "3", None, "corentin.leroy@insa-lyon.fr")
corentin.insererDansCollection()'''
