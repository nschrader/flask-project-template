import sys
import pymongo
from pprint import pprint
from bson.objectid import ObjectId
import utilisateur
import pays
import universite

from pymongo import MongoClient
client = MongoClient('localhost', 27017)

# Base de données
db = client.database

# Collections
utilisateurs = db.utilisateurs
universites = db.universites
collection_pays = db.collection_pays

# Affiche tous les documents de la collection
def afficheCollection(collection) :
    tout = collection.find()
    for document in tout :
        pprint(document)

# Renvoie le document correspondant
def trouverDocument(collection, id) :
    return collection.find({"_id" : id})

# Supprime le document correspondant
def supprimerDocument(collection, id) :
    collection.remove({"_id":id})

# Renvoie un objet Utilisateur correspondant au document d'_id id
def getUtilisateur(id) :
    liste = utilisateurs.find({'_id':id})
    document = liste.__getitem__(0)
    return utilisateur.Utilisateur(document['_id'], document['prenom'], document['nom'], document['departement'], document['niveau'], document['mobilite'], document['mail'])

# Renvoie un objet Pays correspondant au document d'_id id
def getPays(id) :
    liste = collection_pays.find({'_id':id})
    document = liste.__getitem__(0)
    return pays.Pays(document['_id'], document['nom'], document['continent'], document['climat'], document['culture'], document['vie_pratique'], document['tourisme'])

# Renvoie un objet Universite correspondant au document d'_id id
def getUniv(id) :
    liste = universites.find({'_id':id})
    document = liste.__getitem__(0)
    return universite.Universite(document['_id'], document['nom'], document['pays'], document['departements'])
