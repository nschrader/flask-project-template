from hashlib import md5
from ..extensions import mongo
from flask_login import UserMixin


class User(UserMixin):
    #TODO: Needs to be ported to mongodb
    id = 666 #db.Column(db.Integer, primary_key=True)
    password = 'oma123' #db.Column(db.String(200), default='')
    name = 'deine Mudda' #db.Column(db.String(100))
    email = 'deine@mudda.de' #db.Column(db.String(200))
    active = True #db.Column(db.Boolean, default=True)

    def is_active(self):
        return self.active
