from overrides import overrides

from extensions import mongo
from .entity import Entity

class Universite(Entity):

    def __init__(self, **entries):
        self.nom = None
        self.pays = None
        self.departements = None
        Entity.__init__(self, **entries)

    @classmethod
    @overrides
    def get_collection(cls):
        return mongo.universites
