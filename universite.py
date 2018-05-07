import sys
import pymongo
from pprint import pprint
from bson.objectid import ObjectId
import db

class Universite :

    def __init__(self, univId, nom, pays, departements) :
        self.id = univId
        self.nom = nom
        self.pays = pays
        self.departements = departements

    def __str__(self) :
        return "Université " + str(self.id) + " : " + self.nom + "(" + self.pays + "), disponible pour les départements " + str(self.departements)

    # Met à jour les variables
    def update(self, **kwargs) :
        if kwargs.get('nom') :
            self.nom = kwargs.get('nom')
        if kwargs.get('pays') :
            self.pays = kwargs.get('pays')
        if kwargs.get('departements') :
            self.departements = kwargs.get('departements')

    # Insère l'université dans la collection universites
    def insererDansCollection(self) :
        if db.universites.find({"_id" : self.id}).count() > 0 :
            print("L'université " + str(self.id) + " existe déjà.", file=sys.stderr)
        else :
            univ = {
                "_id" : self.id,
                "nom" : self.nom,
                "pays" : self.pays,
                "departements" : self.departements,
            }
            db.universites.insert_one(univ)
