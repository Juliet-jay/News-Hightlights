from app import app
import urllib.request,json
from .models import sources,article



Source = sources.Sources
Article = article.Article


#getting api key
api_key = app.config['NEWS_API_KEY']

#getting source url
sources_base_url = app.config['NEWS_SOURCES_BASE_URL']
article_base_url = app.config['NEWS_ARTICLES_BASE_URL']

#getting article base url
#getting the base urls
# headlines_base_url = None
# everything_base_url = None
# sources_base_url = None
# sources_article_base_url = None

# def configure_request(app):
#         global api_key, headlines_base_url, everything_base_url, sources_base_url, sources_article_base_url
#         api_key = 'dae9480f7d12456fb06a80eceefc97b7'
#         print(api_key)
#         headlines_base_url = app.config["HEADLINES_API_BASE_URL"]
#         print(headlines_base_url.format(api_key))
#         everything_base_url = app.config["EVERYTHING_API_BASE_URL"]
#         sources_base_url = app.config["SOURCES_API_BASE_URL"]
#         sources_article_base_url = app.config["SOURCES_ARTICLE_API_BASE_URL"]



# def process_results(headlines_list):
#         '''
#         Processes headlines results and returns a list of objects
#         '''
#         headlines_results = []
#         for headline_item in headlines_list:
#                 author = headline_item.get('author')
#                 title = headline_item.get('title')
#                 description = headline_item.get('description')
#                 url = headline_item.get('url')
#                 urlToImage = headline_item.get('urlToImage')
#                 publishedAt = headline_item.get('publishedAt')
#                 content = headline_item.get('content')

#                 if author and urlToImage and content:
#                         headlines_object = Headlines(author, title, description, url, urlToImage, publishedAt, content)
#                         headlines_results.append(headlines_object)
#         return headlines_results
                        


def get_sources(category):
    
    
    '''
    Gets the json response to our url request
    '''
    get_sources_url = sources_base_url.format(category, api_key)

    with urllib.request.urlopen(get_sources_url) as url:
            get_sources_data = url.read()
            get_sources_response = json.loads(get_sources_data)

            sources_results = None

            if get_sources_response['sources']:
                
                sources_results_list = get_sources_response['sources']
                sources_results = process_sources(sources_results_list)

    return sources_results

def process_sources(sources_list):
    
    """
    Process list of sources and returns list of source objects
    """
    source_results = []
    
    for source in sources_list:
        
        id = source.get("id")
        name = source.get("name")
        description = source.get("description")
        url = source.get("url")
        category = source.get("category")
        language = source.get("language")
        country = source.get("country")
        
        if description:   
                     
            new_source = Source(id, name, description, url, category, language, country)
            source_results.append(new_source)
            
            
            
    return source_results
    
def get_article(id):
    
    get_article_url = article_base_url.format(id,api_key)
    
    with urllib.request.urlopen(get_article_url) as url:
        
        get_article_data = url.read()
        get_article_response = json.loads(get_article_data)

        article_results = None

        if get_article_response['articles']:
            
            article_results_list = get_article_response['articles']
            article_results = process_articles(article_results_list)

    return article_results

def process_articles(article_result_list):
    
    '''
    this function process the article and returns result list
    '''
    
    article_results=[]
    
    for article in article_result_list:
        
        author = article.get('author')
        title = article.get('title')
        description = article.get('description')
        url = article.get ('url')
        urlToImage = article.get ('urlToImage')
        publishedAt = article.get('publishedAt')
        content = article.get('content')
        
        if urlToImage:
            new_article= Article(author,title,description,url,urlToImage,publishedAt,content)
            article_results.append(new_article)
        
    return article_results

    
    

   
    
    
    


        
