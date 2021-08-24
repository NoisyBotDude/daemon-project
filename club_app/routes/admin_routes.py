from flask import Blueprint, render_template, flash, url_for, redirect, request

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
        club_name = request.form["club-name"]
        club_description = request.form["description"]
        club_registration_link = request.form["registration-link"]
        db.clubs.insert_one(
            {
                "club name": club_name,
                "club description": club_description,
                "club registration link": club_registration_link
            }
        )
        flash(f"{club_name} is added successfully to the database.", "Success")
        return redirect(url_for("admin.option"))


    @admin.route("/club/update", methods = ["GET"])
    def update():
            return render_template("admin/club_update.html", title="Update Club")


    @admin.route("/club/update_response", methods = ["POST", "PUT"])
    def update_response():
        if request.method == "POST":
            club_name = request.form["club-name"]
            portion_to_update = request.form["portion-update"]
            updated_info = request.form["information"]
        db.clubs.update_one(
            {"club name": club_name},
            {
                "$set": {
                    f"{portion_to_update.lower()}": f"{updated_info}"
                }
            }
        )
        flash(f"{club_name} is updated successfully in the database.", "Success")
        return redirect(url_for("admin.option"))

    @admin.route("/club/delete", methods=["GET", "POST"])
    def delete():
        return render_template("admin/club_delete.html", title="Delete Club")

    @admin.route("/club/delete_response", methods=["POST", "DELETE"])
    def delete_response():
        club_name = request.form["club-name"]
        db.clubs.delete_many({"club name": f"{club_name}"})
        flash(f"{club_name} is deleted successfully from the database.", "Success")
        return redirect(url_for("admin.option"))

    
    return admin