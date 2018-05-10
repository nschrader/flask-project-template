from overrides import overrides

from extensions import mongo
from .entity import Entity

class Departement(Entity):

    def __init__(self, **entries):
        self.nom = None
        Entity.__init__(self, **entries)

    @classmethod
    @overrides
    def get_collection(cls):
        return mongo.departement
