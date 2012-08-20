import socket

production_hostnames = ['']

class Config(object):
    DEBUG = False
    TESTING = False
    GOOGLE_MAPS_KEY = ''
    TW_OAUTH_KEY = ''
    TW_OAUTH_SECRET = ''
    SECRET_KEY = ''

    FB_APP_ID = ''
    FB_APP_SECRET = ''

class ProductionConfig(Config):
    MONGO_URI = ''
    MONGO_DB = ''
    SERVER_NAME = ''

class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    MONGO_URI = ''
    MONGO_DB = ''
    SERVER_NAME = ''


class UnitTestingConfig(TestingConfig):
    MONGO_DB = ''

if socket.gethostname() in production_hostnames:
    CONFIGURATION = ProductionConfig
else:
    CONFIGURATION = TestingConfig

