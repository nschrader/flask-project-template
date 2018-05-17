from overrides import overrides

from extensions import mongo
from .enumeration import Enumeration

class Pays(Enumeration):

    def __init__(self, **entries):
        self.climat = None
        self.culture = None
        self.vie_pratique = None
        self.tourisme = None
        self.continent = None
        super().__init__(**entries)


    @classmethod
    def get_from_continent(cls, continent):
        documents = cls.get_collection().find({'continent': continent})
        return cls.make_from_documents(documents)


    @classmethod
    @overrides
    def get_collection(cls):
        return mongo.pays
