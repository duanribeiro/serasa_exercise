from flask import Flask
from flask_pymongo import PyMongo
from flask_jwt_extended import JWTManager
from flask_cors import CORS

mongo = PyMongo()
jwt = JWTManager()


def create_app():
    app = Flask(__name__)

    try:
        if app.config["ENV"] == "production":
            app.config.from_object("config.ProdConfig")
        else:
            app.config.from_object("config.DevConfig")
    except:
        if app.config["ENV"] == "production":
            app.config.from_object("api.config.ProdConfig")
        else:
            app.config.from_object("api.config.DevConfig")


    mongo.init_app(app)
    jwt.init_app(app)

    from api.app.v1 import v1_blueprint
    app.register_blueprint(v1_blueprint)

    CORS(app)
    return app
