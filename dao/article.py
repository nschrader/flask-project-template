from datetime import datetime
from mongoengine import *

from .audit import Audit

class Article(Audit, EmbeddedDocument):
    text = StringField(required = True)
