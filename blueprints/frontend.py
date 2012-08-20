from flask import Blueprint, render_template, abort, redirect, request, g, session, url_for
import json
from werkzeug.wrappers import Request,Response
from functools import wraps
from twython import Twython
from pymongo.errors import DuplicateKeyError
from passlib.hash import sha256_crypt

Frontend = Blueprint('frontend',__name__)

def login_required(f):
    @wraps(f)
    def wrapper(*args,**kwargs):
        if 'user' not in session:
            return redirect('/login')
        return f(*args,**args)
    return wrapper

@Frontend.route('/')
def root():
    """
    Render out the homepage
    """
    return render_template('root.html')

@Frontend.route('/logout')
def logout():
    """
    Log the current user out of the app
    """
    session.pop('user',None)
    return redirect(url_for('.root'))

@Frontend.route('/session')
def show_session():
    """
    Show the current session for debug purposes
    """
    if CONFIGURATION.DEBUG:
        try:
            return '%s'  % (session['user'])
        except KeyError:
            return 'Not logged in'
    else:
        redirect(url_for('.root'))

@Frontend.route('/bagger/<path:template>')
def bagger(template):
    """
    Let vinny do design at this endpoint

    :param template: Select a static template file to output to the browser
    """
    return render_template(template)
