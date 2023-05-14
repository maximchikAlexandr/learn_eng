import os

from dotenv import load_dotenv

load_dotenv()

yandexDictonaryKey = os.getenv("yandexDictonaryKey")


class ConfigurationBase:
    SECRET_KEY = os.getenv("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql+psycopg2://{os.getenv('DB_USER')}:"
        f"{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:"
        f"{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Configuration(ConfigurationBase):
    DEBUG = False


class ConfigurationTest(ConfigurationBase):
    DEBUG = True
