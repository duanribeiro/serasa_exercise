from api.app.v1 import api
from flask_restplus import fields


auth_payload = api.model('Auth', {
    'username': fields.String(required=True, description='username'),
    'password': fields.String(required=True, description='password'),
})
