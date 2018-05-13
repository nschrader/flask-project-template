from bson.objectid import ObjectId

class Entity():
    """All entities are flat, i.e. they do not contain any sub objects just as
    Mongo documents do not contain any sub documents. If you need to reference
    another object (aka document), put its ObjectId into the corresponding field.
    If you need multiple references, use an array for the ObjectIds. """

    def __init__(self, **entries):
        self._id = None
        for k, v in entries.items():
            if k in self.__dict__:
                self.__dict__[k] = v
            else:
                raise AttributeError


    def update(self, **kwargs):
        self.__dict__.update(**kwargs)


    def insert(self):
        if self.__class__.get_collection().find({"_id" : self._id}).count() > 0:
            raise FileExistsError
        else:
            self.override()


    def override(self):
        document = self.__dict__
        document.pop("_id", None)
        self._id = self.__class__.get_collection().insert_one(document).inserted_id

    @classmethod
    def get(cls, id):
        document = cls.get_collection().find_one({'_id': ObjectId(id)})
        if not document:
            return None
        else:
            entity = object.__new__(cls)
            entity.__init__(**document)
            return entity

    @classmethod
    def get_collection(cls):
        raise NotImplementedError
