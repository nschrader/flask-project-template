from overrides import overrides

from extensions import mongo
from .entity import Entity

class Article(Entity):

    def __init__(self, **entries):
        self.text = None
        super().__init__(**entries)


    @overrides
    def update(self, *__weak__, **entries):
        super().update(**entries)


    @classmethod
    @overrides
    def get_collection(cls):
        return mongo.articles
