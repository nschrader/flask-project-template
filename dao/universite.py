from overrides import overrides

from extensions import mongo
from .enumeration import Enumeration

class Universite(Enumeration):

    def __init__(self, *__weak__, **entries):
        self.pays = None
        self.infos = None
        self.departements = None
        self.accords = []
        super().__init__(*__weak__, **entries)

    @overrides
    def update(self, *__weak__, **entries):
        super().update(**entries)
        super().require_list(self.accords)

    @classmethod
    @overrides
    def get_collection(cls):
        return mongo.universites
