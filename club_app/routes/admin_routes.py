from flask import Blueprint, render_template, flash, url_for, redirect, request, session
from club_app.database.database import ClubDataBase
from club_app.database.organise_club_data import organise_data
from club_app.database.image_manipulation import save_image

def create_blueprint(cluster):
    admin = Blueprint("admin", __name__, url_prefix="/admin/club")
    db = cluster.db

    def is_logged_in(func):
        def wrapper():
            if not session.get("name"):
                flash("Authentication required!!!")
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
        club_logo = request.files['club-logo']
        
        data = {
                "club name": club_name,
                "club description": request.form["description"],
                "club recruitement": request.form["recruitement"],
                "club website": request.form["website-link"],
                "club facebook": request.form["facebook-link"],
                "club twitter": request.form["twitter-link"],
                "club instagram": request.form["instagram-link"],
                "club youtube": request.form["youtube-link"],
                "club achievements": request.form["achievements"],
                "club core members":  request.form["core-members"],
                "club contact details": request.form["contact-details"]
            }
        organised_data = organise_data(data)
        ClubDataBase.add_club(organised_data)
        save_image(club_logo, club_name)
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
        return render_template("admin/club_update_name.html", title="Update Club")

    @admin.route("/update_response", methods = ["POST", "PUT"])
    @is_logged_in
    def update_response():
        club_name = request.args.get("club_name")
        if request.method == "POST":
            update_choice = request.form["choice"]
            updated_info = request.form["information"]
            #for member update
            member_name = request.form["member_name"]
            member_update = request.form["member_update"]
            #for contact update
            contact_member_name = request.form["members"]
            contact_update = request.form["member_contact"]


            club = {"club name": club_name}
            data = {
                    "$set": {
                        f"{update_choice}": f"{updated_info}"
                    }
                }
            
            ClubDataBase.update_club(club, data)

            if request.form["member_name"]:

                print(member_name, member_update)
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