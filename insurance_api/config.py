from os import path, environ

from dotenv import load_dotenv

"""App configuration"""

basedir = path.abspath(path.dirname(__file__))
# load_dotenv(path.join(basedir, '../.env'))
load_dotenv(path.join(basedir, '../.env-docker'))


class Config(object):
    # Database
    DB_HOST = environ.get('DB_HOST')
    DB_PORT = environ.get('DB_PORT')
    DB_NAME = environ.get('DB_NAME')
    DB_USER = environ.get('DB_USER')
    DB_PASS = environ.get('DB_PASS')
    TORTOISE_DATABASE_URI = f'postgres://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    # TORTOISE_DATABASE_URI="postgres://postgres:postgres@db:5433/db_server"