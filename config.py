from distutils.command import config
from distutils.debug import DEBUG
import os


class Config:
    '''
    General configuration parent class
    ''' 
    QUOTES_BASE_URL = 'http://quotes.stormconsultancy.co.uk/random.json'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:R0707318659@localhost/blog'
    SECRET_KEY = os.environ.get('SECRET_KEY') 
    UPLOADED_PHOTOS_DEST ='app/static/photos'

     #email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class ProdConfig(Config):
    '''
    Production Configuration class

    Args:
      Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL').replace("://", "ql://", 1)


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:R0707318659@localhost/blog_test'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:R0707318659@localhost/comments_test'

class DevConfig(Config):
    '''
    Development configuration child class 

    Args:
      Config: The parent configuration class with General configuration settings
    '''
    DEBUG = True

config_options = {
  'development': DevConfig,
  'production': ProdConfig,
  'test': TestConfig
}    