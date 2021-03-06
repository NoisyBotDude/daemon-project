from club_app.database.database import ClubDataBase
from flask import Blueprint, render_template, request
from club_app.utils.send_email import send_email
import os
from posixpath import abspath


def create_blueprint(cluster):
    user = Blueprint("user", __name__)
    db = cluster.db

    @user.route("/")
    @user.route("/home")
    def home():
        club_name = ClubDataBase.find_club_name()
        club_count = ClubDataBase.count()
        return render_template("user/home.html",
                               club_name=club_name,
                               club_count=club_count,
                               title="Home"
                               )

    @user.route("/clubs/<string:club_name>")
    def club_info(club_name):
        club_infos = ClubDataBase.find_club(club_name)
        image_exists = os.path.exists(
            abspath(f"club_app\static\images\club_logo\{club_name}.jpg"))

        return render_template("user/club_info.html",
                               club_infos=club_infos,
                               image_exists=image_exists,
                               title=club_name
                               )

    @user.route("/about")
    def about():
        return render_template("user/about.html", title="About Us")

    @user.route("/contact-us", methods=["GET", "POST"])
    def contact():
        if request.method == "POST":
            name = request.form["name"]
            email = request.form["email"]
            comment = request.form["comment"]

            send_email(f"Name: {name}\nEmail: {email}\nComment: {comment}")
        return render_template("user/contact.html", title="Contact Us")

    return user
