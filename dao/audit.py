from datetime import datetime
from mongoengine import *

from .std_user_proxy import StdUserProxy
from .audit_query_set import AuditQuerySet

class Audit():
    meta = {
        'abstract': True,
        'queryset_class': AuditQuerySet
    }

    modified_user = ReferenceField("Utilisateur", default = StdUserProxy.get)
    modified_time = DateTimeField(default = datetime.now)


    def save(self, *args, **kwargs):
        self.modified_date = datetime.now()
        self.modified_user = StdUserProxy.get()
        return super().save(*args, **kwargs)


    def saveAndGet(self):
        self.save()
        return self
