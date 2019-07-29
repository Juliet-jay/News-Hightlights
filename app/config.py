class Config:
    '''
    General configuration parent class
    '''
    
    NEWS_SOURCES_BASE_URL='https://newsapi.org/v2/sources?category={}&apiKey={}'
    NEW_ARTICLES_BASE_URL='https://newsapi.org/v2/everything?sources={}&apiKey={}'

class ProdConfig(Config):
    '''
    Production Configuration child class
    Args:
        Config:The parent configuration class with General configuration settings
    '''
    pass

class DevConfig(Config):
    '''
    Development Configuration child class
    Args:
        Config:The parent configuration class with General configuration settings
    '''
    DEBUG = True
