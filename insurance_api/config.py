from os import path, environ

from dotenv import load_dotenv

"""App configuration"""

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '../.env'))


class Config(object):
    # Database
    TORTOISE_DATABASE_URI = environ.get('TORTOISE_DATABASE_URI')
