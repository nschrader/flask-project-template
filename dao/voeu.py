from datetime import datetime
from mongoengine import *

from .audit import Audit

class Voeu(Audit, Document):
    utilisateur = ReferenceField("Utilisateur", required = True)
    universite = ReferenceField("Universite", required = True)
