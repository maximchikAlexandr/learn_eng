class ConfigurationBase(object):
    SECRET_KEY = 'eeda3f35d9d4482f6eb1d34c11ccb08781633acf'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///dct/data/dct_eng.db'
    SQLALCHEMY_BINDS = {'user_bp' : 'sqlite:///user/data/users.db'}
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Configuration(ConfigurationBase):
    DEBUG = False


class ConfigurationTest(ConfigurationBase):
    DEBUG = True

