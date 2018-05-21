from werkzeug.security import generate_password_hash, check_password_hash
from overrides import overrides
from flask_login import UserMixin
from mongoengine import *

import config

class Utilisateur(UserMixin, Document):
    nom = StringField(required = True)
    prenom = StringField(required = True)
    departement = ReferenceField("Departement")
    niveau = IntField()
    mobilites = ListField(ReferenceField("Universite"))
    mail = EmailField(required = True, domain_whitelist = ["insa-lyon.fr"], unique = True)
    password = StringField(required = True)
    admin = BooleanField(default = False)


    def get_nom(self):
        return "{} {}".format(self.prenom, self.nom)


    @overrides
    def get_id(self):
        return str(self.pk)


    def validate_login(self, password):
        return check_password_hash(self.password, password)


    @staticmethod
    def get_root():
        root_user = Utilisateur.objects(mail = config.ROOT).first()
        if not root_user:
            password = generate_password_hash(config.ROOT_PSWD)
            root_user = Utilisateur(
                mail = config.ROOT,
                password = config.ROOT_PSWD,
                nom = config.ROOT,
                prenom = "",
                admin = True
            )
            root_user.save()
        return root_user
