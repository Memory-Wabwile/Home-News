from flask import render_template
from app import app

#views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    message = 'Hello World'
    return render_template('index.html' , message=message)


@app.route('/article/<int:id>')
def article(id):
    '''
    view news and returns the news details
    '''
    article = article_source(id)
    return render_template('article.html' , articles = articles , id=id)
        
