from flask import render_template
from app import app
from .request import get_source , get_articles , get_headlines , get_category 

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


@app.route('/category/<category_name>')
def category(category_name):
    '''
    function that returns all the categories
    '''
    title = f'{category_name}'
    category = get_category(category_name)
    catgory = category_name

    return render_template ('category.html' , title = title , category = category , catgory = category_name)
    
        
