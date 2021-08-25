from club_app.database.database import DataBase
from flask import Blueprint, render_template
import json

def create_blueprint(cluster):
    user = Blueprint("user",__name__)
    db = cluster.db


    @user.route("/")
    @user.route("/home")
    def home():
        return render_template("user/home.html")

    @user.route("/clubs/<string:club_name>")
    def club_info(club_name):
        club_info = DataBase.find_club(club_name)
        return render_template("user/club_info.html", club_info=club_info)

    return user
