from werkzeug.security import generate_password_hash
from . import *

from extensions import mongo

class Utilisateur :

    def __init__(self, uId, prenom, nom, departement, niveau, mobilite, mail) :
        self.id = uId
        self.nom = nom
        self.prenom = prenom
        self.departement = departement
        self.niveau = niveau
        self.mobilite = mobilite
        self.mail = mail

    def __str__(self) :
        return "Utilisateur " + str(self.id) + " : " + self.prenom + " " + self.nom + ", " + str(self.niveau) + self.departement + ", mobilite : " + str(self.mobilite) + ", " + self.mail

    # Met à jour les variables
    def update(self, **kwargs) :
        if kwargs.get('prenom') :
            self.prenom = kwargs.get('prenom')
        if kwargs.get('nom') :
            self.nom = kwargs.get('nom')
        if kwargs.get('departement') :
            self.departement = kwargs.get('departement')
        if kwargs.get('niveau') :
            self.niveau = kwargs.get('niveau')
        if kwargs.get('mobilite') :
            self.mobilite = kwargs.get('mobilite')
        if kwargs.get('mail') :
            self.mail = kwargs.get('mail')

    # Insère l'utilisateur dans la collection utilisateurs
    def insererDansCollection(self) :
        if db.utilisateurs.find({"_id" : self.id}).count() > 0 :
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
            db.utilisateurs.insert_one(utilisateur)

#TODO: Put this into class
def make_root(root, root_pswd):
    if not mongo.users.find_one({"_id": root}):
        hash = generate_password_hash(root_pswd, method='pbkdf2:sha256')
        mongo.users.insert({"_id": root, "password": hash})
