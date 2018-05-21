from mongoengine import *

from .audit import Audit

class Continent(Audit, Document):
    nom = StringField(unique = True)
