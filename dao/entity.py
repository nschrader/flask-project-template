from bson.objectid import ObjectId
from datetime import datetime

class Entity():
    """All entities are flat, i.e. they do not contain any sub objects just as
    Mongo documents do not contain any sub documents. If you need to reference
    another object (aka document), put its ObjectId into the corresponding field.
    If you need multiple references, use an array for the ObjectIds. """

    def __init__(self, *__weak__, **entries):
        self._id = None
        self.modify = None
        self.get_user(**entries)
        self.update(*__weak__, **entries)


    def update(self, *__weak__, **entries):
        for k, v in entries.items():
            if k in self.__dict__:
                self.__dict__[k] = v
            elif not True in __weak__:
                raise AttributeError(k)
        if not True in __weak__:
            self.modify = datetime.now()
        return self


    def insert(self):
        if self.__class__.get_collection().find({"_id" : self._id}).count() > 0:
            raise FileExistsError(self._id)
        else:
            self.override()
        return self


    def override(self):
        document = self.__dict__
        if not self._id:
            document.pop("_id", None)
        self._id = self.__class__.get_collection().insert_one(document).inserted_id
        return self


    def remove(self):
        if not self.__class__.get_collection().delete_one({"_id": self._id}).deleted_count:
            raise FileNotFoundError(self._id)

    std_user = None
    def get_user(self, **entries):
        if "user" in entries:
            self.user = entries["user"]
        elif self.__class__.std_user:
            self.user = self.__class__.std_user
        else:
            raise AttributeError("Neither defined \"std_user\" nor passed \"user\"")


    @classmethod
    def make(cls, *__weak__, **entries):
        entity = object.__new__(cls)
        entity.__init__(*__weak__, **entries)
        return entity


    @classmethod
    def get(cls, id):
        _id = id if isinstance(id, ObjectId) else ObjectId(id)
        document = cls.get_collection().find_one({'_id': _id})
        if not document:
            return None
        else:
            return cls.make(True, **document)


    @classmethod
    def get_all(cls):
        documents = cls.get_collection().find()
        return [cls.make(True, **document) for document in documents]


    @classmethod
    def get_collection(cls):
        raise NotImplementedError

    @staticmethod
    def require_list(lst):
        if not isinstance(lst, list):
            raise AttributeError(lst)
