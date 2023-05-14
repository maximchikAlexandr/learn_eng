import os

from dotenv import load_dotenv

load_dotenv()

yandex_dictionary_key = os.getenv("YANDEX_DICTIONARY_KEY")


class ConfigurationBase:
    SECRET_KEY = os.getenv("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql+psycopg2://{os.getenv('POSTGRES_USER')}:"
        f"{os.getenv('POSTGRES_PASSWORD')}@{os.getenv('DB_HOST')}:"
        f"{os.getenv('DB_PORT')}/{os.getenv('POSTGRES_DB')}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Configuration(ConfigurationBase):
    DEBUG = False


class ConfigurationTest(ConfigurationBase):
    DEBUG = True
