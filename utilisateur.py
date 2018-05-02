import sys
import pymongo
from pprint import pprint
from bson.objectid import ObjectId

from pymongo import MongoClient
client = MongoClient('localhost', 27017)

# Base de données
db = client.database

# Collections
utilisateurs = db.utilisateurs
universites = db.universites
pays = db.pays

# Affiche tous les documents de la collection
def afficheTout(collection) :
    tout = collection.find()
    for document in tout :
        pprint(document)

# Insère un utilisateur dans la collection utilisateurs
def insererUtilisateur(uId, nom, prenom, departement, niveau, mobilite, mail) :
    if utilisateurs.find({"_id" : uId}).count() > 0 :
        print("L'utilisateur " + str(uId) + " existe déjà.", file=sys.stderr)
    else :
        utilisateur = {
            "_id" : uId,
            "nom" : nom,
            "prenom" : prenom,
            "departement" : departement,
            "niveau" : niveau,
            "mobilite" : mobilite,
            "mail" : mail
        }
        utilisateurs.insert_one(utilisateur)

#insererUtilisateur(69, "Corentin", "Leroy", "TC", "3", None, "corentin.leroy@insa-lyon.fr")

# Insère un pays dans la collection pays
def insererPays(paysId, nom, continent, climat, culture, vie_pratique, tourisme, universites) :
    if pays.find({"_id" : paysId}).count() > 0 :
        print("Le pays " + str(paysId) + " existe déjà.", file=sys.stderr)
    else :
        nouveauPays = {
            "_id" : paysId,
            "nom" : nom,
            "climat" : climat,
            "culture" : culture,
            "vie_pratique" : vie_pratique,
            "tourisme" : tourisme,
            "universites" : universites
        }
        pays.insert_one(nouveauPays)

# Insère une université dans la collection universites
def insererUniv(univId, continent, pays, nom, departements) :
    if universites.find({"_id" : univId}).count() > 0 :
        print("L'université " + str(univId) + " existe déjà.", file=sys.stderr)
    else :
        univ = {
            "_id" : univId,
            "continent" : continent,
            "pays" : pays,
            "nom" : nom,
            "departements" : departements,
        }
        universites.insert_one(univ)
