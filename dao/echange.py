from mongoengine import *

from .audit import Audit

class Echange(Audit, EmbeddedDocument):
    accord = ReferenceField("Accord", required = True)
    departements = ListField(ReferenceField("Departement"), required = True)
    places = StringField()


    def get_departments_str(self):
        return ", ".join(d.nom for d in self.departements)


    def get_summary_str(self):
        dpts = self.get_departments_str()
        return "{} ({}): {} places".format(self.accord.nom, dpts, self.places)
