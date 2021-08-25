from os import environ
from flask import Flask
from flask_pymongo import PyMongo
from . import config
from .routes import admin_routes, user_routes
from .database.database import DataBase

def create_app():
    """Creating and returning app object"""    

    app = Flask(__name__)
    app.config.from_object(config.Development())
    cluster = PyMongo(app)
    DataBase.initialize(cluster)

    """Note: Blueprint is used to separate routes into different
             folders and files for better organization of files
    """


    """Registering blueprints"""

    app.register_blueprint(admin_routes.create_blueprint(cluster))
    app.register_blueprint(user_routes.create_blueprint(cluster))

    return app

