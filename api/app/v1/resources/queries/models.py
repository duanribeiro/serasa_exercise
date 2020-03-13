import json
from app import mongo
from flask_restplus import abort
from bson.json_util import dumps

from quotes.helpers.auth import AuthEncrypt



class Auth:

    @staticmethod
    def change_username_password(payload):
        username = payload.get('username')
        password = payload.get('password')
        password = password.encode()

        auth = AuthEncrypt(password)
        encrypted_password = auth.encrypt_password()

        mongo.db.auth.update_one({},
                                 {"$set": {"username": username, "password": encrypted_password}},
                                 upsert=True)

        return 'ok'

class Quotes:

    @staticmethod
    def get_all():
        results = mongo.db.quotes.find({}, {"_id": 0})

        return json.loads(dumps(results))
