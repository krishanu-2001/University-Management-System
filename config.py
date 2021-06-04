from os import environ, path
from dotenv import load_dotenv
import yaml

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))
db = yaml.load(open('db.yaml'))

class Config:
    """Base config."""
    SECRET_KEY = environ.get('SECRET_KEY')
    SESSION_COOKIE_NAME = environ.get('SESSION_COOKIE_NAME')
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = environ.get('MAIL_PASSWORD')


class ProdConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False
    #add database for production here


class DevConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = False
    MYSQL_HOST = db['mysql_host']
    MYSQL_USER = db['mysql_user']
    MYSQL_PASSWORD = db['mysql_password']
    MYSQL_DB = db['mysql_db']
    MYSQL_PORT = db['mysql_port']
    