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
    title = 'News Highlight- Fast and reliable way to get news'
    return render_template('index.html', title = title,sport_sources=sport_sources)


# @app.route("/sources_articles/<source_id>")
# def source_articles(source_id):
#     """
#     View function for a specific source's articles
#     """
#     articles = get_sources_articles(source_id)
#     title = source_id
#     return render_template("source_articles.html", articles = articles, title=title)

