from overrides import overrides

from extensions import mongo
from .enumeration import Enumeration

class Universite(Enumeration):

    def __init__(self, **entries):
        self.pays = None
        self.infos = None
        self.departements = None
        self.accords = []
        super().__init__(**entries)


    @overrides
    def update(self, **entries):
        super().update(**entries)
        super().require_list(self.accords)


    @classmethod
    def get_from_pays(cls, pays):
        documents = cls.get_collection().find({'pays': pays})
        return cls.make_from_documents(documents)


    @classmethod
    @overrides
    def get_collection(cls):
        return mongo.universites
