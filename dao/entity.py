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
        if not self._id:
            document.pop("_id", None)
        self._id = self.__class__.get_collection().insert_one(document).inserted_id


    def remove(self):
        if not self.__class__.get_collection().delete_one({"_id": self._id}).deleted_count:
            raise FileNotFoundError


    @classmethod
    def make(cls, **args):
        entity = object.__new__(cls)
        entity.__init__(**args)
        return entity


    @classmethod
    def get(cls, id):
        _id = id if isinstance(id, ObjectId) else ObjectId(id)
        document = cls.get_collection().find_one({'_id': _id})
        if not document:
            return None
        else:
            return cls.make(**document)


    @classmethod
    def get_all(cls):
        documents = cls.get_collection().find()
        return [cls.make(**document) for document in documents]


    @classmethod
    def get_collection(cls):
        raise NotImplementedError
