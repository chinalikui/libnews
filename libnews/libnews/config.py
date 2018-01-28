import os

class Basic(object):
    DEBUG = True
    CSRF_ENABLED = True
    SECRET_KEY = 'aljfnxkjfwfsfddfj'
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://likui:post200ed@localhost:5432/test?client_encoding=utf-8"


class Production(object):
    DEBUG = True
    CSRF_ENABLED = True
    SECRET_KEY = 'aljfnxkjfwfsfddfj'
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://likui:post200ed@localhost:5432/test?client_encoding=utf-8"



config = {
        'basic':Basic,
        'production':Production,
        }

