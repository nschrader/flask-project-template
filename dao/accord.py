from overrides import overrides

from extensions import mongo
from .entity import Entity

class Accord(Entity):

    def __init__(self, *__weak__, **entries):
        self.type = None
        self.departements = []
        super().__init__(*__weak__, **entries)


    @overrides
    def update(self, *__weak__, **entries):
        super().update(**entries)
        super().require_list(self.departements)


    @classmethod
    def get_from_departement(cls, dpt):
        documents = cls.get_collection().find({"departements": dpt})
        return cls.make_from_documents(documents)


    @classmethod
    @overrides
    def get_collection(cls):
        return mongo.accords
