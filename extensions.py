import config

from flask_mail import Mail
mail = Mail()

from mongoengine import connect
connect(config.DB)

from flask_login import LoginManager
login_manager = LoginManager()

from markdown import markdown
