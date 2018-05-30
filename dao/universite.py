from mongoengine import *
from .pays import Pays
from .departement import Departement
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
    def get_choices(cls):
        unis = [(univ.pk, univ.nom) for univ in cls.objects.all()]
        return sorted(unis, key=lambda x: x[1])


    @classmethod
    def get_choices_with_departement(cls, departement):
        unis = [(univ.pk, univ.nom) for univ in cls.objects.all() if [d for e in univ.echanges for d in e.departements if d == departement]]
        return sorted(unis, key=lambda x: x[1])
