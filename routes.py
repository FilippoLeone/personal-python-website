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
    tools = Tools
    return dict(
        year=datetime.now().year,
        version=tools.GetVersion('version')
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