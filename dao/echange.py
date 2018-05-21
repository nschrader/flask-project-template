from mongoengine import *

from .audit import Audit

class Echange(Audit, EmbeddedDocument):
    accord = ReferenceField("Accord", required = True)
    departements = ListField(ReferenceField("Departement"), required = True)
    places = StringField()
