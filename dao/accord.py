from mongoengine import *

from .audit import Audit

class Accord(Audit, Document):
    nom = StringField(unique = True)
