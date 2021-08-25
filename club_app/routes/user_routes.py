from club_app.database.database import DataBase
from flask import Blueprint, render_template, jsonify
import json

def create_blueprint(cluster):
    user = Blueprint("user",__name__)
    db = cluster.db


    @user.route("/")
    @user.route("/home")
    def home():
        return render_template("user/home.html")

    return user