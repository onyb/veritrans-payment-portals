import os


class Config(object):
    DEBUG = False
    ROOT_DIR = os.environ['HOME']


class Prod(Config):
    DEBUG = False
    MONGO_URL = os.environ['MONGO_URL']


class Dev(Config):
    DEBUG = True
    MONGO_URL = {
        'host': 'mongodb://USERNAME:PASSWORD@HOST',
    }