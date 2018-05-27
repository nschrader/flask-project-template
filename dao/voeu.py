from datetime import datetime
from overrides import overrides
from mongoengine import *

from .audit import Audit

class Voeu(EmbeddedDocument):
    universite = ReferenceField("Universite", required = True)
    annee = IntField()
    semestre = IntField(min_value = 1, max_value = 2)
    modified_time = DateTimeField(default = datetime.now)


    @overrides
    def save(self, *args, **kwargs):
        self.modified_date = datetime.now()
        return super().save(*args, **kwargs)


    @staticmethod
    def get_semestre_choices():
        return [("1", "S1"), ("2", "S2")]
