class Configuration(object):
    DEBUG = False
    SECRET_KEY = 'eeda3f35d9d4482f6eb1d34c11ccb08781633acf'

class ConfigurationTest(object):
    DEBUG = True
    SECRET_KEY = 'eeda3f35d9d4482f6eb1d34c11ccb08781633acf'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///dct/dct_eng.db'
    SQLALCHEMY_BINDS = {'user_bp' : 'sqlite:///user/users.db'}
    SQLALCHEMY_TRACK_MODIFICATIONS = False
