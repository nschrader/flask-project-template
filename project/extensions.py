from flask_mail import Mail
mail = Mail()

from pymongo import MongoClient
mongo = MongoClient().projectWhiskey

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.login_view = 'login'
