from flask import render_template
from app import app
from .request import get_source , get_articles , get_headlines

#views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - News'
    sources= get_source()
    headlines = get_headlines()
    return render_template('index.html' , title=title , sources = sources , headlines = headlines)


@app.route('/article/<id>')
def article(id):
    '''
    view news and returns the news details
    '''
    articles = get_articles(id)
    return render_template('article.html' , articles = articles , id=id)
        
