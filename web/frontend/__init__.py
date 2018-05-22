import sys, inspect

from .views import *
from dao import *

__daos__ = inspect.getmembers(sys.modules["dao"], inspect.isclass)
app.jinja_env.globals.update(**dict(__daos__))
