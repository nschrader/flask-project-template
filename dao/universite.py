from mongoengine import *

from .audit import Audit

class Universite(Audit, Document):
    nom = StringField(required = True, unique = True)
    pays = ReferenceField("Pays", required = True)
    cours = EmbeddedDocumentField("Article")
    accessibilite = EmbeddedDocumentField("Article")
    logement = EmbeddedDocumentField("Article")
    ambiance = EmbeddedDocumentField("Article")
    echanges = EmbeddedDocumentListField("Echange")


    @classmethod
    def get_with_echanges_for_pays(cls, pays):
        us = cls.objects(pays=pays)
        return [(u, e) for u in us for e in u.echanges]
