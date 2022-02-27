from app import app
import urllib.request,json
from .models import article
from .models import sources


Article = article.Article

#Getting api key
apiKey = app.config['NEWS_API_KEY'] 

#GEtting the article base url
base_url = app.config["NEWS_API_BASE_URL"]

# getting source ase url
base_url_source = app.config['NEWS_API_SOURCE_URL']


def get_source ():
    '''
    Function that gets the json response to our url request
    '''
    get_base_url_source = base_url_source.format(apiKey)

    with urllib.request.urlopen(get_base_url_source) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        source_results = None

        if get_sources_response['sources']:
            source_results_list = get_sources_response['sources']
            source_results = process_results(source_results_list)

    return source_results


def process_source_results(sources_list):
    '''
     Function  that processes the articles result and transform them to a list of Objects
    '''
    source_list = []
    for source in source_list:
       id = source.get('id')
       name = source.get('name')
       description = source.get('description')
       url = source.get('url')
       

       if id:
           source_object = Source(id , name ,description ,url )
           source_list.append(source_object)

    return source_list


def get_articles ():
    '''
    Function that gets the json response to our url request
    '''
    get_articles_url = base_url.format(apiKey)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        article_results = None

        if get_articles_response['results']:
            article_results_list = get_articles_response['results']
            article_results = process_results(article_results_list)

    return article_results


def process_results(article_list):
    '''
     Function  that processes the articles result and transform them to a list of Objects
    '''
    article_list = []
    for article in article_list:
       author = article.get('author')
       title = article.get('title')
       description = article.get('description')
       publishedAt = article.get('publishedAt')
       content = article.get('content')
       url = article.get('url')
       image = article.get('urlToImage')
       

       if url:
           article_item = Article(author , title , description , publishedAt , content ,url ,urlToImage)
           article_list.append(article_item)

    return article_list