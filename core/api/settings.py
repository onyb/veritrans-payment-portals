import os


class _Config(object):
    DEBUG = True
    TESTING = False

    ROOT_DIR = os.environ['HOME']


class Prod(_Config):
    DEBUG = False
    TESTING = False
    MONGODB_SETTINGS = {
        'host': 'mongodb://USERNAME:PASSWORD@HOST',
    }


class Dev(_Config):
    NAME = "Dev"
    DEBUG = True
    MONGODB_SETTINGS = {
        'host': 'mongodb://USERNAME:PASSWORD@HOST',
    }


class Testing(_Config):
    NAME = "Test"
    TESTING = True
    MONGODB_SETTINGS = {
        'db': 'test_db'
    }
