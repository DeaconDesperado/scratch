from flask import Flask,request,abort,redirect
from werkzeug.wrappers import Request,Response
import json
from werkzeug.serving import run_simple
from blueprints.frontend import Frontend
from config import CONFIGURATION

app = Flask(__name__)
app.config.from_object(CONFIGURATION)
app.register_blueprint(Frontend)
app.register_blueprint(Frontend,subdomain='www')
application = app

if __name__ == '__main__':
    app.debug = True
    run_simple('',5050,app,use_reloader=True,use_debugger=True)
