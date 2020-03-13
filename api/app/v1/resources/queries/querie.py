from flask_restplus import Resource, Namespace
from app import mongo
from app.v1.resources.queries.serializers import auth_payload
from api.app.v1.resources.queries.models import Auth, Quotes


api = Namespace('', 'Endpoints')

@api.route('/')
class Endpoints(Resource):
    # @api.marshal_list_with(queries)
    @api.expect(auth_payload)
    @api.doc(responses={
        200: 'Success',
        400: 'Bad Request',
    })
    def put(self):
        """
        Update the username and password for scrapy website
        """

        return Auth.change_username_password(payload=api.payload)

    @api.doc(responses={
        200: 'Success',
        400: 'Bad Request',
    })
    def get(self):
        """
        Get the information of quotes on database
        """

        return Quotes.get_all()


    @api.doc(responses={
        200: 'Success',
        400: 'Bad Request',
    })
    def post(self):
        """
        Run the crawler
        """
        import subprocess
        spider_name = "quotes"
        subprocess.check_output(['scrapy', 'crawl', spider_name])

        return 'ok'
