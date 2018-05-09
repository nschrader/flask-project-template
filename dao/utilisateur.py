from werkzeug.security import generate_password_hash, check_password_hash
from bson.objectid import ObjectId
from overrides import overrides
from flask_login import UserMixin

from extensions import mongo

class Utilisateur(UserMixin):

    def __init__(self, **entries):
        self._id = None
        self.nom = None
        self.prenom = None
        self.departement = None
        self.niveau = None
        self.mobilite = None
        self.mail = None
        self.password = None
        if entries:
            self.__dict__.update(entries)

    def update(self, **kwargs):
        self.__dict__.update(**kwargs)


    def insert(self):
        if mongo.utilisateurs.find({"_id" : self._id}).count() > 0:
            raise FileExistsError
        else :
            document = self.__dict__
            document.pop("_id", None)
            self._id = mongo.utilisateurs.insert_one(document).inserted_id


    @staticmethod
    def get(id):
        document = mongo.utilisateurs.find_one({'_id': ObjectId(id)})
        if not document:
            return None
        else:
            return Utilisateur(**document)


    @staticmethod
    def get_mail(mail):
        document = mongo.utilisateurs.find_one({'mail': mail})
        if not document:
            return None
        else:
            return Utilisateur(**document)


    # Flask-Login method, our identification is by mail
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
