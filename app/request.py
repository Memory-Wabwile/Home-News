from app import app
import urllib.request,json
from .models import article

Article = article.Article

#Getting api key
apiKey = app.config['NEWS_API_KEY'] 

#GEtting the article base url
base_url = app.config["NEWS_API_BASE_URL"]

def get_articles