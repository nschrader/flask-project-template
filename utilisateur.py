import sys
import pymongo
from pprint import pprint
from bson.objectid import ObjectId

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.database
utilisateurs = db.utilisateurs

class Utilisateur :

    def __init__(self, uId, nom, prenom, departement, niveau, mobilite, mail) :
        self.id = uId
        self.nom = nom
        self.prenom = prenom
        self.departement = departement
        self.niveau = niveau
        self.mobilite = mobilite
        self.mail = mail

    # Insère un utilisateur dans la collection utilisateurs
    def insererDansCollection(self) :
        if utilisateurs.find({"_id" : self.id}).count() > 0 :
            print("L'utilisateur " + str(self.id) + " existe déjà.", file=sys.stderr)
        else :
            utilisateur = {
                "_id" : self.id,
                "nom" : self.nom,
                "prenom" : self.prenom,
                "departement" : self.departement,
                "niveau" : self.niveau,
                "mobilite" : self.mobilite,
                "mail" : self.mail
            }
            utilisateurs.insert_one(utilisateur)
