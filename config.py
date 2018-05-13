import os

class Config(object):
    
    # Security
    DEBUG = True
    SECRET_KEY = 'ngjqVmXKmqfKN46jKIzj'
    ROOT = "superuser"
    ROOT_PSWD = "yoMama"

    # Mail
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = 'dont.reply.to.project.whiskey'
    MAIL_PASSWORD = 'webWEB123'
    MAIL_DEFAULT_SENDER = 'Project Whiskey <dont.reply.to.project.whiskey@gmail.com>'

    # Auth
    SESSION_COOKIE_NAME = 'session'
