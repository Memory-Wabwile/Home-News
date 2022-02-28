import os

class Config:
    '''
    General configuration parent class
    '''
    #The api key
    # NEWS_API_KEY = 'NEWS_API_KEY'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    #The sources url
    NEWS_API_SOURCE_URL = 'https://newsapi.org/v2/sources?apiKey={}'
    #The articles url
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/top-headlines?country=us&category={}&apiKey={}'
    #secret key
    # SECRET_KEY = os.environ.get('SECRET_KEY')


class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
    Config: The parent configuration class with General configuration settings
    '''
    pass

class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
    Config: The parent configuration class with General configuration settings
    '''
    DEBUG = True

config_options = {
    'development' : DevConfig,
    'production' : ProdConfig
}