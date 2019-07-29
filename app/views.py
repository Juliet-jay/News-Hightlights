from flask import render_template
from app import app
from .request import get_sources

#Views
@app.route ('/')
def index():
    '''
    Returns index page and its data
    '''

    #Getting the news sources
    sport_sources = get_sources('sports')
    business_sources = get_sources('business')
    entertainment_sources = get_sources('entertainment')
    health_sources = get_sources('health')
    general_sources = get_sources('general')
    tech_sources = get_sources('tech')
    title = 'News Highlight- Fast and reliable way to get news'
    return render_template('index.html', title = title,sport_sources=sport_sources,business_sources=business,entertainment_sources=entertainment_sources,health_sources=health_sources,general_sources=general_sources,tech_sources=tech_sources)


# @app.route("/sources_articles/<source_id>")
# def source_articles(source_id):
#     """
#     View function for a specific source's articles
#     """
#     articles = get_sources_articles(source_id)
#     title = source_id
#     return render_template("source_articles.html", articles = articles, title=title)

