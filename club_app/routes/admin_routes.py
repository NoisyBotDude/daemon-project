from flask import Blueprint, render_template, flash, url_for, redirect, request, session
from club_app.database.database import ClubDataBase
from club_app.database.organise_club_data import organise_data

def create_blueprint(cluster):
    admin = Blueprint("admin", __name__, url_prefix="/admin/club")
    db = cluster.db

    def is_logged_in(func):
        def wrapper():
            if not session.get("name"):
                flash("Authendication required!!!")
                return redirect(url_for("admin_auth.admin_home"))
            return func()
        wrapper.__name__ = func.__name__
        return wrapper

    @admin.route("/", methods=["GET"])
    @is_logged_in
    def option():
        return render_template("admin/form_option.html", title="Admin options")

    @admin.route("/add", methods=["GET"])
    @is_logged_in
    def add():
        return render_template("admin/club_add.html", title="Add Club")

    @admin.route("/add_response", methods = ["POST"])
    @is_logged_in
    def add_response():
        club_name = request.form["name"]
        club_description = request.form["description"]
        club_recruitement = request.form["recruitement"]
        club_website = request.form["website-link"]
        club_facebook = request.form["facebook-link"]
        club_twitter = request.form["twitter-link"]
        club_instagram = request.form["instagram-link"]
        club_youtube = request.form["youtube-link"]
        club_achievements = request.form["achievements"]
        club_core_members = request.form["core-members"]
        club_contact_details = request.form["contact-details"]
        
        data = {
                "club name": club_name,
                "club description": club_description,
                "club recruitement": club_recruitement,
                "club website": club_website,
                "club facebook": club_facebook,
                "club twitter": club_twitter,
                "club instagram": club_instagram,
                "club youtube": club_youtube,
                "club achievements": club_achievements,
                "club core members": club_core_members,
                "club contact details": club_contact_details
            }
        organised_data = organise_data(data)
        ClubDataBase.add_club(organised_data)
        flash(f"{club_name} is added successfully to the database.", "Success")
        return redirect(url_for("admin.option"))


    @admin.route("/update", methods = ["GET", "POST"])
    @is_logged_in
    def update():
        if request.method == "POST":
            club_name = request.form["club-name"]
            club_infos = ClubDataBase.find_club(club_name)
            return render_template("admin/club_update.html", title="Update Club", \
                                    club_name=club_name, club_infos=club_infos)
        else:
            return render_template("admin/club_update_name.html", title="Update Club")

    @admin.route("/update_response", methods = ["POST", "PUT"])
    @is_logged_in
    def update_response():
        if request.method == "POST":
            club_name = request.form["club-name"]
            portion_to_update = request.form["choice"]
            updated_info = request.form["information"]


        club = {"club name": club_name}
        data = {
                "$set": {
                    f"{portion_to_update}": f"{updated_info}"
                }
            }
        ClubDataBase.update_club(club, data)
        flash(f"{club_name} is updated successfully in the database.", "Success")
        return redirect(url_for("admin.option"))

    @admin.route("/delete", methods=["GET", "POST"])
    @is_logged_in
    def delete():
        return render_template("admin/club_delete.html", title="Delete Club")

    @admin.route("/delete_response", methods=["POST", "DELETE"])
    @is_logged_in
    def delete_response():
        club_name = request.form["club-name"]
        club = {"club name": f"{club_name}"}
        ClubDataBase.delete_club(club)
        flash(f"{club_name} is deleted successfully from the database.", "Success")
        return redirect(url_for("admin.option"))

    
    return admin