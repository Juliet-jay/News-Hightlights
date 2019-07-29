
import urllib.request,json
from .models import Sources,Article


#getting api key
api_key = None

#Getting the news base url
sources_base_url = None
article_base_url = None

def configure_request(app):
    global api_key,sources_base_url,article_base_url  
    api_key=app.config["NEWS_API_KEY"]
    sources_base_url = app.config['NEWS_SOURCES_BASE_URL']
    article_base_url = app.config['NEWS_ARTICLES_BASE_URL']


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
                     
            new_source = Sources(id, name, description, url, category, language, country)
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

    
    

   
    
    
    


        
