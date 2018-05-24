from extensions import login_manager

from .views import *
from .anonymous_user import AnonymousUser

login_manager.anonymous_user = AnonymousUser
login_manager.login_view = "login"
login_manager.refresh_view = "login"
login_manager.needs_refresh_message = "Afin de protéger votre compte, veuillez vous reconnecter."
login_manager.needs_refresh_message_category = "info"
