from club_app.database.database import ClubDataBase
from flask import Blueprint, render_template

def create_blueprint(cluster):
    user = Blueprint("user",__name__)
    db = cluster.db

    @user.route("/")
    @user.route("/home")
    def home():
        club_name = ClubDataBase.find_club_name()
        club_count = ClubDataBase.count()
        return render_template("user/home.html", club_name=club_name, club_count=club_count)

    @user.route("/clubs/<string:club_name>")
    def club_info(club_name):
        club_infos = ClubDataBase.find_club(club_name)
        return render_template("user/club_info.html", club_infos=club_infos)

    @user.route("/about")
    def about():
        return render_template("user/about.html")

    @user.route("/contact-us")
    def contact():
        return render_template("user/contact.html")

    return user
