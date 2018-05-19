from werkzeug.security import generate_password_hash, check_password_hash
from overrides import overrides
from flask_login import UserMixin

from extensions import mongo
from .entity import Entity

class Utilisateur(UserMixin, Entity):

    def __init__(self, **entries):
        self.nom = None
        self.prenom = None
        self.departement = None
        self.niveau = None
        self.mobilites = []
        self.mail = None
        self.password = None
        self.admin = None
        UserMixin.__init__(self)
        Entity.__init__(self, **entries)
        del self.user

    @overrides
    def update(self, **entries):
        super().update(**entries)
        super().require_list(self.mobilites)

    @overrides
    def insert(self):
        if self.__class__.get_collection().find({"mail" : self.mail}).count() > 0:
            #raise FileExistsError(self.mail)
            self.__class__.get_collection().remove({"mail" : self.mail})
        return Entity.insert(self)


    def get_nom(self):
        return "{} {}".format(self.prenom, self.nom)


    @overrides
    def __get_user__(self, **entries):
        return


    @classmethod
    @overrides
    def get_collection(cls):
        return mongo.utilisateurs


    @classmethod
    def get_mail(cls, mail):
        document = cls.get_collection().find_one({'mail': mail})
        return cls.make_from_document(document)


    @overrides
    def get_id(self):
        return str(self._id)


    def validate_login(self, password):
        return check_password_hash(self.password, password)


    @staticmethod
    def make_root(root, root_pswd):
        root_user = Utilisateur.get_mail(root)
        if not root_user:
            password = generate_password_hash(root_pswd)
            root_user = Utilisateur(
                mail=root,
                password=password,
                nom=root,
                prenom="",
                admin=True
            )
            root_user.insert()
        return root_user
