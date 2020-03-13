from flask import Blueprint
from flask_restplus import Api

v1_blueprint = Blueprint('v1', __name__, url_prefix='/api/v1')

api = Api(v1_blueprint,
          doc='/docs',
          title='API Documentation',
          version='1.0',
          description='Flask RESTful API')

from .resources.queries.querie import api as querie_ns



api.add_namespace(querie_ns)


