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

#Create Read Update Delete

# Affiche tous les documents de la collection
def afficheCollection(collection) :
    tout = collection.find()
    for document in tout :
        pprint(document)

# Renvoie le document correspondant
def trouverDocument(collection, id) :
    return collection.find({"_id" : id})

# Renvoie un objet Utilisateur correspondant au document d'_id id
def getUtilisateur(id) :
    liste = utilisateurs.find({'_id':id})
    document = liste.__getitem__(0)
    return Utilisateur(document['_id'], document['nom'], document['prenom'], document['departement'], document['niveau'], ['mobilite'], document['mail'])

# Tests
'''corentin = Utilisateur(69, "Leroy", "Corentin", "TC", "3", None, "corentin.leroy@insa-lyon.fr")
corentin.insererDansCollection()
coco = getUtilisateur(69)
print(coco.prenom)'''
