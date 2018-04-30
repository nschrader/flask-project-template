from hashlib import md5
from ..extensions import mongo
from flask_login import UserMixin


class User(UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(200), default='')
    name = db.Column(db.String(100))
    email = db.Column(db.String(200))
    active = db.Column(db.Boolean, default=True)

    def is_active(self):
        return self.active
