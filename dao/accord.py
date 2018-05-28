from mongoengine import *

from .audit import Audit

class Accord(Audit, Document):
    nom = StringField(unique = True)

    @classmethod
    def get_choices(cls):
        return [(a.pk, a.nom) for a in cls.objects.all()]
