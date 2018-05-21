from mongoengine import *

from .audit import Audit

class Universite(Audit, Document):
    nom = StringField(required = True, unique = True)
    pays = ReferenceField("Pays", required = True)
    infos = EmbeddedDocumentField("Article")
    echanges = EmbeddedDocumentListField("Echange")
