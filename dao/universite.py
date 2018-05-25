from mongoengine import *
from .departement import Departement
from .audit import Audit

class Universite(Audit, Document):
    nom = StringField(required = True, unique = True)
    pays = ReferenceField("Pays", required = True)
    infos = EmbeddedDocumentField("Article")
    echanges = EmbeddedDocumentListField("Echange")


    def get_infos_html(self):
        return Markup(markdown(self.infos.text))


    @classmethod
    def get_with_echanges_for_pays(cls, pays):
        us = cls.objects(pays=pays)
        return [(u, e) for u in us for e in u.echanges]


    @classmethod
    def get_with_echanges_for_pays_and_departement(cls, pays, departement):
        us = cls.objects(pays=pays)
        dpt = Departement.objects.with_id(departement)
        return [(u, e) for u in us for e in u.echanges if dpt in e.departements]
