class Sources:
    '''
    source class that defines the news source
    '''
    
    def __init__(self,id,name,description,url,category,language,country): 
        
        self.id=id
        self.name=name
        self.description=description
        self.url=url
        self.category=category
        self.language=language
        self.country=country

class Article:
    '''
    Article class that defines the articles objects
    '''

    def __init__(self,author,title,description,url,urlToImage,publishedAt,content):
        self.author=author
        self.title=title
        self.description=description
        self.url=url
        self.urlToImage=urlToImage
        self.publishedAt=publishedAt
        self.content=content

