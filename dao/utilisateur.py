from werkzeug.security import generate_password_hash, check_password_hash
from overrides import overrides
from flask_login import UserMixin
from uuid import uuid4 as uuid
from datetime import datetime
from mongoengine import *

import config
import dao.voeu

class Utilisateur(UserMixin, Document):
    nom = StringField(required = True)
    prenom = StringField(required = True)
    mail = EmailField(required = True, domain_whitelist = ["insa-lyon.fr"], unique = True)
    password = StringField(required = True)
    token = StringField()
    token_timestamp = DateTimeField()
    active = BooleanField(default = False)
    admin = BooleanField(default = False)

    departement = ReferenceField("Departement")
    niveau = IntField()
    mobilites = ListField(ReferenceField("Universite"))
    voeux_annee = IntField()
    voeu_1 = EmbeddedDocumentField("Voeu")
    voeu_2 = EmbeddedDocumentField("Voeu")


    def get_nom(self):
        return "{} {}".format(self.prenom, self.nom)


    def make_token(self):
        self.token = uuid().hex
        self.token_timestamp = datetime.now()


    @overrides
    def get_id(self):
        return str(self.pk)


    @property
    @overrides
    def is_active(self):
        return self.active


    def validate_login(self, password):
        return check_password_hash(self.password, password)


    @classmethod
    #TODO: Use endm instead of -1, 0, 1
    def verifify_token(cls, token):
        user = cls.objects(token = token).first()
        if user:
            timediff = datetime.now() - user.token_timestamp
            if timediff.total_seconds() < config.TOKEN_TIMEOUT:
                if timediff.total_seconds() < config.TOKEN_VALIDITY_TIMEOUT:
                    user.active = True
                    user.save()
                    return 1
                else:
                    return 0
        return -1



    @classmethod
    def get_root(cls):
        root_user = cls.objects(mail = config.ROOT).first()
        if not root_user:
            password = generate_password_hash(config.ROOT_PSWD)
            root_user = Utilisateur(
                mail = config.ROOT,
                password = password,
                nom = "Root",
                prenom = "Admin",
                admin = True,
                active = True
            )
            root_user.save()
        return root_user


    @staticmethod
    def get_annee_choices():
        return [("2", "2A"), ("3", "3A"), ("4", "4A"), ("5", "5A")]
