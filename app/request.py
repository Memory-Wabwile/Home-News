
import urllib.request,json
from .models import Article , Source , Headlines ,Category



#Getting api key
apiKey = None

#GEtting the article base url
base_url = None

# getting source ase url
base_url_source = None

def configure_request(app):
    global apiKey , base_url , base_url_source
    apiKey = app.config['NEWS_API_KEY'] 
    base_url = app.config["NEWS_API_BASE_URL"]
    base_url_source = app.config['NEWS_API_SOURCE_URL']




def get_source():
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
            source_results = process_source_results(source_results_list)

    return source_results


def process_source_results(sources_list):
    '''
     Function  that processes the articles result and transform them to a list of Objects
    '''
    source_list = []
    for source in sources_list:
       id = source.get('id')
       name = source.get('name')
       description = source.get('description')
       url = source.get('url')
       

       if id:
           source_object = Source(id , name ,description ,url )
           source_list.append(source_object)

    return source_list


def get_articles (id):
    '''
    Function that gets the json response to our url request
    '''
    get_articles_url = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'.format(id,apiKey)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        article_results = None

        if get_articles_response['articles']:
            article_results_list = get_articles_response['articles']
            article_results = process_results(article_results_list)

    return article_results


def process_results(articles_list):
    '''
     Function  that processes the articles result and transform them to a list of Objects
    '''
    article_list = []
    for article in articles_list:
       author = article.get('author')
       title = article.get('title')
       description = article.get('description')
       publishedAt = article.get('publishedAt')
       content = article.get('content')
       url = article.get('url')
       image = article.get('urlToImage')
       

       if url:
           article_item = Article(author , title , description , publishedAt , content ,url ,image)
           article_list.append(article_item)

    return article_list


def get_headlines():
    '''
    Function that gets the json response to our url request
    '''
    get_headlines_url = 'https://newsapi.org/v2/top-headlines?country=us&apiKey={}'.format(apiKey)

    with urllib.request.urlopen(get_headlines_url) as url:
        get_headlines_data = url.read()
        get_headlines_response = json.loads(get_headlines_data)

        get_headlines_results = None

        if get_headlines_response['articles']:
            get_headlines_list = get_headlines_response['articles']
            get_headlines_results = process_results(get_headlines_list)

    return get_headlines_results


def get_category(category_name):
    '''
    Function that gets the json response to our url request
    '''
    get_category_url = base_url.format(category_name,apiKey)

    with urllib.request.urlopen(get_category_url) as url :
        get_category_data = url.read()
        get_category_response = json.loads(get_category_data)

        get_category_results = None

        if get_category_response['articles']:
            get_category_list = get_category_response['articles']
            get_category_results = process_results(get_category_list)

    return get_category_results


