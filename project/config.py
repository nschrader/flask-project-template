import os

DEBUG = True
SECRET_KEY = 'ngjqVmXKmqfKN46jKIzj'

# flatpages
FLATPAGES_EXTENSION = '.md'
FLATPAGES_ROOT = os.path.join(os.path.dirname(__file__), 'docs')

# make sure that you have started debug mail server using command
# $ make mail
MAIL_SERVER = 'localhost'
MAIL_PORT = 20025
MAIL_USE_SSL = False
MAIL_USERNAME = 'your@email.address'
#MAIL_PASSWORD = 'topsecret'

# Auth
SESSION_COOKIE_NAME = 'session'
