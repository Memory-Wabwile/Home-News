class Article:
    '''
    Article class to define the articles objects
    '''
    def __init__(self , author , title , description , publishedAt , content , url , urlToImage ):
        self.author = author
        self.title = title
        self.description = description
        self.publishedAt = publishedAt
        self.content = content
        self.url = url
        self.urlToImage = urlToImage

    

class Source : 
    '''
    source class to define the source objects
    '''
    def __init__(self , id , name , description , url):
        self.id = id
        self.name = name
        self.description = description
        self.url = url


class Headlines:
    '''
    Headlines class to define the headlines objects
    '''
    def __init__(self , author , title , description , publishedAt , content , url , urlToImage  ):
        self.author = author
        self.title = title
        self.description = description
        self.publishedAt = publishedAt
        self.content = content
        self.url = url
        self.urlToImage = urlToImage


class Category:
    '''
     Headlines class to define the headlines objects
    '''
       
    def __init__(self , author , title , description , publishedAt , content , url , urlToImage  ):
        self.author = author
        self.title = title
        self.description = description
        self.publishedAt = publishedAt
        self.content = content
        self.url = url
        self.urlToImage = urlToImage