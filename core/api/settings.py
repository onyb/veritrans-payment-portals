import os


class Config(object):
    DEBUG = False
    ROOT_DIR = os.environ['HOME']


class Prod(Config):
    DEBUG = False
    MONGO_URI = os.environ['MONGO_URI']


class Dev(Config):
    DEBUG = True
    MONGO_URI = {
        'host': 'mongodb://USERNAME:PASSWORD@HOST',
    }