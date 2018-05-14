from overrides import overrides

from extensions import mongo
from .enumeration import Enumeration

class Pays(Enumeration):

    def __init__(self, *__weak__, **entries):
        self.climat = None
        self.culture = None
        self.vie_pratique = None
        self.tourisme = None
        self.continent = None
        super().__init__(*__weak__, **entries)


    @classmethod
    @overrides
    def get_collection(cls):
        return mongo.pays
