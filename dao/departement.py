from mongoengine import *

from .audit import Audit

class Departement(Audit, Document):
    nom = StringField(unique = True)
