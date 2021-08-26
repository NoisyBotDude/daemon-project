from flask import Blueprint, render_template, flash, url_for, redirect, request
from club_app.database.database import DataBase

def create_blueprint(cluster):
    admin = Blueprint("admin",__name__,url_prefix="/admin")
    db = cluster.db

    @admin.route("/club", methods=["GET"])
    def option():
        return render_template("admin/form_option.html", title="Admin options")

    @admin.route("/club/add", methods=["GET"])
    def add():
        return render_template("admin/club_add.html", title="Add Club")

    @admin.route("/club/add_response", methods = ["POST"])
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
        DataBase.add_club(data)
        flash(f"{club_name} is added successfully to the database.", "Success")
        return redirect(url_for("admin.option"))


    @admin.route("/club/update", methods = ["GET"])
    def update():
            return render_template("admin/club_update.html", title="Update Club")


    @admin.route("/club/update_response", methods = ["POST", "PUT"])
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
        DataBase.update_club(club, data)
        flash(f"{club_name} is updated successfully in the database.", "Success")
        return redirect(url_for("admin.option"))

    @admin.route("/club/delete", methods=["GET", "POST"])
    def delete():
        return render_template("admin/club_delete.html", title="Delete Club")

    @admin.route("/club/delete_response", methods=["POST", "DELETE"])
    def delete_response():
        club_name = request.form["club-name"]
        club = {"club name": f"{club_name}"}
        DataBase.delete_club(club)
        flash(f"{club_name} is deleted successfully from the database.", "Success")
        return redirect(url_for("admin.option"))

    
    return admin