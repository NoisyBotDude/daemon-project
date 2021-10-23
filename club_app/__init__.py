from os import environ
from flask import Flask, session
from flask_pymongo import PyMongo
from flask_session import Session
from . import config
from .routes import admin_routes, user_routes
from .admin_auth import auth_routes
from .database.database import ClubDataBase, AdminDataBase

def create_app():
    """Creating and returning app object"""

    app = Flask(__name__)
    app.config.from_object(config.Development())
    cluster = PyMongo(app)
    # Session(app)
    ClubDataBase.initialize(cluster)
    AdminDataBase.initialize(cluster)


    """Note: Blueprint is used to separate routes into different
             folders and files for better organization of files
    """

    """Registering blueprints"""

    app.register_blueprint(admin_routes.create_blueprint(cluster))
    app.register_blueprint(user_routes.create_blueprint(cluster))
    app.register_blueprint(auth_routes.create_blueprint())

    return app

