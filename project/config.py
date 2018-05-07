import os

# Security
DEBUG = True
SECRET_KEY = 'ngjqVmXKmqfKN46jKIzj'
ROOT = "superuser"
ROOT_PSWD = "yoMama"

# Flatpages
FLATPAGES_EXTENSION = '.md'
FLATPAGES_ROOT = os.path.join(os.path.dirname(__file__), 'docs')

# Mail
MAIL_SERVER = 'smtp.yandex.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USERNAME = 'project.whiskey@yandex.com'
MAIL_PASSWORD = 'webWEB123'

# Auth
SESSION_COOKIE_NAME = 'session'
