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

class ProdConfig(Config):
    '''
    Production Configuration class

    Args:
      Config: The parent configuration class with General configuration settings
    '''
    pass

class DevConfig(Config):
    '''
    Development configuration child class 

    Args:
      Config: The parent configuration class with General configuration settings
    '''
    DEBUG = True

config_options = {
  'development': DevConfig,
  'production': ProdConfig
}    