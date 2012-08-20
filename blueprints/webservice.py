from flask import Blueprint, render_template, abort, redirect, request, g, session
import json
from werkzeug.wrappers import Request,Response
from functools import wraps
from flask.views import MethodView

from pxquilt.models.patch import Patch
from pxquilt.models.user import User
from pxquilt.encoder import Encoder
from pxquilt.config import CONFIGURATION

from bson.objectid import ObjectId
from pymongo.errors import DuplicateKeyError
from passlib.hash import sha256_crypt

WebService = Blueprint('webservice',__name__)

def login_required(f):
    @wraps(f)
    def wrapper(*args,**kwargs):
        if 'user' not in session:
            return json.dumps({'flag':0,'msg':'Action requires authentication'})
        return f(*args,**args)
    return wrapper

