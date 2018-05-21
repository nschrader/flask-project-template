from mongoengine import *

import dao.article
from .audit import Audit

class Pays(Audit, Document):
    nom = StringField(unique = True)
    climat = EmbeddedDocumentField("Article")
    culture = EmbeddedDocumentField("Article")
    vie_pratique = EmbeddedDocumentField("Article")
    tourisme = EmbeddedDocumentField("Article")
    continent = ReferenceField("Continent")
