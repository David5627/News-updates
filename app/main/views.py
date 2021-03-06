from flask import render_template, request, url_for, redirect
from . import main
from ..request import  get_sources, get_articles


@main.route('/')
def index():

     '''
    View root page function that returns the index page and its data
    '''

     title = "welcome to your best broadcasting channel"
     sources = get_sources()
     #news sources array here, passed then for-looped
     return render_template('index.html', title = title, sources = sources)


#articles
@main.route('/articles/<names>')
def articles(names):
     '''
     View root page function that returns the index page and its data
     '''
     name = names 
     print("here")
     articles = get_articles(names)
     return render_template('articles.html', name = names, articles = articles)