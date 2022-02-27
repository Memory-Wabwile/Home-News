class Headlines:
    '''
    source class to define the source objects
    '''
    def __init__(self , author , title , description , publishedAt , content , url , urlToImage  ):
        self.author = author
        self.title = title
        self.description = description
        self.publishedAt = publishedAt
        self.content = content
        self.url = url
        self.urlToImage = urlToImage