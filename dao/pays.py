from mongoengine import *
from flask import Markup

import dao.article
from extensions import markdown
from .audit import Audit

class Pays(Audit, Document):
    nom = StringField(unique = True)
    climat = EmbeddedDocumentField("Article")
    culture = EmbeddedDocumentField("Article")
    vie_pratique = EmbeddedDocumentField("Article")
    tourisme = EmbeddedDocumentField("Article")
    continent = ReferenceField("Continent")


    def get_climat_html(self):
        return Markup(markdown(self.climat.text))


    def get_culture_html(self):
        return Markup(markdown(self.culture.text))


    def get_vie_pratique_html(self):
        return Markup(markdown(self.vie_pratique.text))


    def get_tourisme_html(self):
        return Markup(markdown(self.tourisme.text))
