from mongoengine import *

from .audit import Audit

class Departement(Audit, Document):
    nom = StringField(unique = True)


    @classmethod
    def get_choices(cls):
        return [(d.pk, d.nom) for d in cls.objects.all()]
