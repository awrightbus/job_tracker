import os

#make sure the secret key is randomly generated in production

class Config(object):
    FLASK_ENV  = 'development'
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.getenv('SECRET_KEY', default='\xc5p]\xdb\xeb*#\xfa\xc7\xf4xW\xea\x7fqdC\xa9\xa7z\x07\x19}\xd8x\xb6\xa0b\xac\xdaE\xd1')


class ProductionConfig(Config):
    FLASK_ENV = 'production'

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True