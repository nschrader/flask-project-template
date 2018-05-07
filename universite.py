import sys
import pymongo
from pprint import pprint
from bson.objectid import ObjectId

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.database
universites = db.universites

class Universite :

    def __init__(self, univId, continent, pays, nom, departements) :
        self.id = univId
        self.continent = continent
        self.pays = pays
        self.nom = nom
        self.departements = departements

    # Insère l'université dans la collection universites
    def insererDansCollection(self) :
        if universites.find({"_id" : self.id}).count() > 0 :
            print("L'université " + str(self.id) + " existe déjà.", file=sys.stderr)
        else :
            univ = {
                "_id" : self.id,
                "continent" : self.continent,
                "pays" : self.pays,
                "nom" : self.nom,
                "departements" : self.departements,
            }
            universites.insert_one(univ)
