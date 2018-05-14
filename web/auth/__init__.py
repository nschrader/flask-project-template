from extensions import login_manager

from .views import *
from .anonymous_user import AnonymousUser

login_manager.anonymous_user = AnonymousUser
login_manager.login_view = 'login'
