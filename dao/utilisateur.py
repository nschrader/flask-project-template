from werkzeug.security import generate_password_hash, check_password_hash
from overrides import overrides
from flask_login import UserMixin

from extensions import mongo
from .entity import Entity
from .departement import Departement

class Utilisateur(UserMixin, Entity):

    def __init__(self, **entries):
        self.nom = None
        self.prenom = None
        self.departement = None
        self.niveau = None
        self.mobilite = None
        self.mail = None
        self.password = None
        Entity.__init__(self, **entries)


    def get_nom(self):
        return "{} {}".format(self.prenom, self.nom)


    @classmethod
    @overrides
    def get_collection(cls):
        return mongo.utilisateurs


    @staticmethod
    def get_mail(mail):
        document = mongo.utilisateurs.find_one({'mail': mail})
        if not document:
            return None
        else:
            return Utilisateur(**document)


    @overrides
    def get_id(self):
        return str(self._id)


    def validate_login(self, password):
        return check_password_hash(self.password, password)


    @staticmethod
    def make_root(root, root_pswd):
        if not Utilisateur.get_mail(root):
            password = generate_password_hash(root_pswd)
            root_user = Utilisateur(mail = root, password = password)
            root_user.insert()
