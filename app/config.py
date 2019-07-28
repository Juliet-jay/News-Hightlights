class Config:
    '''
    General configuration parent class
    '''
    
    NEWS_SOURCES_BASE_URL='https://newsapi.org/v2/sources?category={}&apiKey={}'
    NEWS_HEADLINES_BASE_URL='https://newsapi.org/v2/top-headlines?sources{}&apiKey={}'
    NEW_ARTICLES_BASE_URL='https://newsapi.org/v2/everything?sources={}&apiKey={}'
