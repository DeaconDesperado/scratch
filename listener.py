from flask import Flask,request,abort,redirect
from werkzeug.wrappers import Request,Response
import json
from werkzeug.serving import run_simple

from blueprints.fb_auth import FB
from blueprints.twitter import Twitter
from blueprints.frontend import Frontend
from blueprints.webservice import WebService
from config import CONFIGURATION

app = Flask(__name__)
app.config.from_object(CONFIGURATION)
app.register_blueprint(WebService,url_prefix='/data',subdomain='')
app.register_blueprint(Frontend)
app.register_blueprint(Frontend,subdomain='www')
app.register_blueprint(WebService,subdomain='data')
app.register_blueprint(FB,url_prefix='/oauth/facebook',subdomain='www')
app.register_blueprint(Twitter,url_prefix='/oauth/twitter',subdomain='www')
app.register_blueprint(FB,url_prefix='/oauth/facebook',subdomain='')
app.register_blueprint(Twitter,url_prefix='/oauth/twitter',subdomain='')
app.register_blueprint(WebService,url_prefix='/data',subdomain='www')
application = app

if __name__ == '__main__':
    app.debug = True
    run_simple('',5050,app,use_reloader=True,use_debugger=True)
