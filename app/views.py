from flask import render_template
from app import app
from .request import get_sources,get_articles

#Views
@app.route('/')
@app.route('/MJ/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    # Getting the news sources
    tech_sources = get_sources('technology')
    entertainment_sources = get_sources('entertainment')
    health_sources = get_sources('health')
    general_sources = get_sources('general')
    science_sources = get_sources('science')
    business_sources = get_sources('business')
    sports_sources = get_sources('sports')

    title = 'MJ News App'
    return render_template('index.html', title=title,tech=tech_sources ,
                           entertainment=entertainment_sources,health=health_sources,general=general_sources, ,
                           science=science_sources,business=business_sources, sports=sports_sources, )


@app.route("/MJ/<source_id>")
def news_source(source_id):
    '''
    View new_source page function that returns a news source page and its data
    '''
    title=f"{source_id}-page"
    articles = get_articles(source_id)
    print(articles)
    return render_template('newsSource.html', title=title,articles=articles)
