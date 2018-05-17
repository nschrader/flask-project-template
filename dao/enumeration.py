from overrides import overrides

from .entity import Entity

class Enumeration(Entity):

    def __init__(self, *__weak__, **entries):
        self.nom = None
        super().__init__(*__weak__, **entries)


    @overrides
    def insert(self):
        if self.__class__.get_collection().find({"nom" : self.nom}).count() > 0:
            raise FileExistsError(self.nom)
        return Entity.insert(self)
