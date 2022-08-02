import os

from dotenv import load_dotenv

load_dotenv()

yandexDictonaryKey  = os.getenv('yandexDictonaryKey')

class ConfigurationBase(object):
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///dct/data/dct_eng.db'
    SQLALCHEMY_BINDS = {'user_bp' : 'sqlite:///user/data/users.db'}
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Configuration(ConfigurationBase):
    DEBUG = False


class ConfigurationTest(ConfigurationBase):
    DEBUG = True

