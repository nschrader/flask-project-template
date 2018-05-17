from bson.objectid import ObjectId
from datetime import datetime

class Entity():
    """All entities are flat, i.e. they do not contain any sub objects just as
    Mongo documents do not contain any sub documents. If you need to reference
    another object (aka document), put its ObjectId into the corresponding field.
    If you need multiple references, use an array for the ObjectIds. """

    def __init__(self, **entries):
        self._id = None
        self.modify = None
        self.user = self.__get_user__(**entries)
        self.update(**entries)


    def update(self, **entries):
        weak = entries.get("__weak__", False)
        for k, v in entries.items():
            if k in self.__dict__:
                self.__dict__[k] = v
            elif not weak:
                raise AttributeError(k)
        if not weak:
            self.modify = datetime.now()
        return self


    def insert(self):
        if self.__class__.get_collection().find({"_id" : self._id}).count() > 0:
            raise FileExistsError(self._id)
        else:
            return self.override()


    def override(self):
        document = self.__dict__
        if not self._id:
            document.pop("_id", None)
        self._id = self.__class__.get_collection().insert_one(document).inserted_id
        return self


    def remove(self):
        if not self.__class__.get_collection().delete_one({"_id": self._id}).deleted_count:
            raise FileNotFoundError(self._id)
        else:
            del self


    std_user = None
    def __get_user__(self, **entries):
        if "user" in entries:
            return entries["user"]
        elif self.__class__.std_user:
            return self.__class__.std_user
        else:
            raise AttributeError("Neither defined \"std_user\" nor passed \"user\"")


    @classmethod
    def make_from_document(cls, document):
        if document:
            entity = object.__new__(cls)
            entity.__init__(__weak__=True, **document)
            return entity
        else:
            return None


    @classmethod
    def make_from_documents(cls, documents):
        return [cls.make_from_document(document) for document in documents]


    @classmethod
    def get(cls, id):
        _id = id if isinstance(id, ObjectId) else ObjectId(id)
        document = cls.get_collection().find_one({'_id': _id})
        return cls.make_from_document(document)


    @classmethod
    def get_all(cls):
        documents = cls.get_collection().find()
        return cls.make_from_documents(documents)


    @classmethod
    def get_collection(cls):
        raise NotImplementedError

    @staticmethod
    def require_list(lst):
        if not isinstance(lst, list):
            raise AttributeError(lst)
