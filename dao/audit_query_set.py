from mongoengine import *
from flask import abort

class AuditQuerySet(QuerySet):
    def get_or_404(self, *args, **kwargs):
        try:
            return self.get(*args, **kwargs)
        except (MultipleObjectsReturned, DoesNotExist, ValidationError):
            abort(404)


    def first_or_404(self):
        obj = self.first()
        if obj is None:
            abort(404)
        return obj


    def id_or_404(self, id):
        try:
            obj = self.with_id(id)
        except (ValidationError):
            obj = None
        if obj is None:
            abort(404)
        return obj
