"""
Routes and views for the bottle application.
"""

from bottle import route, view, request
from datetime import datetime
from main import Tools,Database
import json

@route('/')
@route('/home')
@view('index')
def home():
    """
    Homepage of the website that contains the database connection.
    """

    # Enstablishing the connection
    with open("db_credentials","r") as blog_pw:
        credentials = blog_pw.readline()
    credentials = credentials.split(";;")
    db = Database.ServerConnect("localhost", credentials[0], credentials[1], "blog", 3306)

    results = Database.QuerySelect(db.cursor(), "blog_post", "*")
    results = [list(results) for element in results]

    return dict(

        year=datetime.now().year,
        version=Tools.GetVersion('version'),

        # Tridimensional, getting -1 to obtain the latest news fetched from the database
        blog_title_1 = results[0][-1][1],
        blog_imagelink_1 = results[0][-1][5],
        article_link_1 = results[0][-1][7],

        blog_title_2 = results[0][-2][1],
        blog_imagelink_2 = results[0][-2][5],
        article_link_2 = results[0][-2][7],

        blog_title_3 = results[0][-3][1],
        blog_imagelink_3 = results[0][-3][5],
        article_link_3 = results[0][-3][7],
    )

@route('/contact')
@view('contact')
def contact():
    """Renders the contact page."""
    return dict(
        title='Contact',
        message='Send me an email.',
        year=datetime.now().year
    )

@route('/dev_blog')
@view('dev_blog')
def about():
    """Renders the about page."""
    return dict(
        title='DevBook',
        message='FAQ.',
        year=datetime.now().year
    )

@route('/latest_cv')
@view('latest_cv')
def latest_cv():
    """ Main page start add more comments here """
    return dict(
        title='LatestCV',
        year=datetime.now().year
    )

@route('/contact_me')
@view('contact_me')
def contact_me():
    """
    Currently just returning a json formatted text.
    // Todo: Implement python mailer or a call to some 3rd party service API 
    """
    email = request.params.get('email')
    bodytext = request.params.get('bodytext')
    return json.dumps({'contact':[email,bodytext]})


@route('/blog')
@view('blog')
def blog():
    """
    The blog section will show the user an infinite cascade of blog posts 
    that will load based on the user scroll.
    """
    return dict(
        title="Blog",
        year=datetime.now().year
        )



if __name__ == '__main__':
    application = default_app()