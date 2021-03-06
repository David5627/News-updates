import os
class Config:
    '''
    General configuration parent class
    '''
    BASE_URL = 'https://newsapi.org/v2/top-headlines?language=en&country={}&apiKey={}'
    BASE_URL_SOURCES = 'https://newsapi.org/v2/sources?language=en&apiKey={}'
    BASE_URL_ARTICLES = 'https://newsapi.org/v2/everything?language=en&sources={}&apiKey={}'
    API_KEY = os.environ.get('API_KEY')
    SECRET_KEY = os.environ.get('david')

class ProdConfig(Config):
    '''
    Pruduction  configuration child class
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
    'development': DevConfig,
    'production': ProdConfig
}