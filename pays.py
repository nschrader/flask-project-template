import sys
import pymongo
from pprint import pprint
from bson.objectid import ObjectId

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.database
pays = db.pays

class Pays :

    def __init__(self, paysId, nom, continent, climat, culture, vie_pratique, tourisme, universites) :
        self.id = paysId
        self.nom = nom
        self.continent = continent
        self.climat = climat
        self.culture = culture
        self.vie_pratique = vie_pratique
        self.tourisme = tourisme
        self.universites = universites

    # Insère un pays dans la collection pays
    def insererDansCollection(self) :
        if pays.find({"_id" : self.id}).count() > 0 :
            print("Le pays " + str(self.id) + " existe déjà.", file=sys.stderr)
        else :
            nouveauPays = {
                "_id" : self.id,
                "nom" : self.nom,
                "climat" : self.climat,
                "culture" : self.culture,
                "vie_pratique" : self.vie_pratique,
                "tourisme" : self.tourisme,
                "universites" : self.universites
            }
            pays.insert_one(nouveauPays)
