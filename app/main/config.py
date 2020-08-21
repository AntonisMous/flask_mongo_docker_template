import os
import logging
# uncomment the line below for postgres database url from environment variable
# postgres_local_base = os.environ['DATABASE_URL']

from constants import PROJECT_NAME, MONGO_HOST

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', PROJECT_NAME + '_secret_key')
    DEBUG = False

    MONGO_DATABASE = PROJECT_NAME
    MONGO_SERVER = 'mongodb://' + MONGO_HOST + ':27017/' + MONGO_DATABASE


class DevelopmentConfig(Config):
    ENVIRONMENT = 'development'
    DEBUG = True
    MONGO_URI = Config.MONGO_SERVER + ENVIRONMENT
    LOGGING_LEVEL = logging.DEBUG


class TestingConfig(Config):
    ENVIRONMENT = 'testing'
    DEBUG = True
    TESTING = True
    MONGO_URI = Config.MONGO_SERVER + ENVIRONMENT
    LOGGING_LEVEL = logging.INFO


class ProductionConfig(Config):
    DEBUG = False
    MONGO_URI = Config.MONGO_SERVER
    LOGGING_LEVEL = logging.WARNING


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY
