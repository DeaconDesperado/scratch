import json
from bson.objectid import ObjectId
import datetime
import dateutil.parser

class Encoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        elif isinstance(obj, datetime.datetime):
            return obj.isoformat()

class Decoder(json.JSONDecoder):
    def decode(self,s):
        return json.JSONDecoder.decode(self,s)
