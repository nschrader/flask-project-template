from . import *

class Pays :

    def __init__(self, paysId, nom, continent, climat, culture, vie_pratique, tourisme) :
        self.id = paysId
        self.nom = nom
        self.continent = continent
        self.climat = climat
        self.culture = culture
        self.vie_pratique = vie_pratique
        self.tourisme = tourisme
        self.universites = []

    def __str__(self) :
        string = "Pays " + str(self.id) + " : " + self.nom + " (" + self.continent + "). Universités : "
        if self.universites == [] :
            string += "aucune"
        else :
            for univ in self.universites :
                string += univ.nom
        return string

    # Met à jour les variables
    def update(self, **kwargs) :
        if kwargs.get('nom') :
            self.nom = kwargs.get('nom')
        if kwargs.get('continent') :
            self.continent = kwargs.get('continent')
        if kwargs.get('climat') :
            self.climat = kwargs.get('climat')
        if kwargs.get('climat') :
            self.climat = kwargs.get('climat')
        if kwargs.get('culture') :
            self.culture = kwargs.get('culture')
        if kwargs.get('vie_pratique') :
            self.vie_pratique = kwargs.get('vie_pratique')
        if kwargs.get('tourisme') :
            self.tourisme = kwargs.get('tourisme')
        listeUniv = db.universites.find({'pays':self.nom})
        for doc in listeUniv :
            self.universites.append(db.getUniv(doc['_id']))

    # Insère le pays dans la collection pays
    def insererDansCollection(self) :
        if db.collection_pays.find({"_id" : self.id}).count() > 0 :
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
            db.collection_pays.insert_one(nouveauPays)
