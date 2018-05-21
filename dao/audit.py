from datetime import datetime
from mongoengine import *

from .std_user_proxy import StdUserProxy

class Audit():
    meta = { 'abstract': True }

    modified_user = ReferenceField("Utilisateur", default = StdUserProxy.get)
    modified_time = DateTimeField(default = datetime.now)

    def saveAndGet(self):
        self.save()
        return self
