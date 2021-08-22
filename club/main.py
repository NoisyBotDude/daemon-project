from flask import Flask, render_template, flash, url_for, redirect
from flask_pymongo import PyMongo
from club_entry_form import *


app = Flask(__name__)
app.config["SECRET_KEY"] = "5791628bb0b13ce0c676dfde280ba245"

mongodb_client = PyMongo(app, uri="mongodb://localhost:27017/TUClubs")
db = mongodb_client.db

@app.route("/club", methods = ["GET", "POST"])
def option():
    option = FormOption()
    if option.club_add_form.data:
        return redirect(url_for("add"))
    elif option.club_update_form.data:
        return redirect(url_for("update"))
    elif option.club_delete_form.data:
        return redirect(url_for("delete"))
    return render_template("form_option.html", option=option)

@app.route("/club/add", methods = ["GET", "POST"])
def add():
    add_form = ClubAdd()
    if add_form.validate_on_submit():
        db.clubs.insert_one(
            {
                "club name":add_form.club_name.data, 
                "club description": add_form.club_description.data, 
                "club registration link": add_form.club_registration_link.data
            }
        )
        flash(f"{add_form.club_name.data} is added successfully to the database.", "Success")
        return redirect(url_for("option"))
    return render_template("club_add.html", title="Club Entry form", add_form=add_form)

@app.route("/club/update", methods = ["GET", "POST"])
def update():
    update_form = ClubUpdate()
    if update_form.validate_on_submit():
        db.clubs.update_one(
            {  "club name":update_form.club_name.data  },
            {
                "$set": {
                    f"{update_form.portion_to_be_updated.data.lower()}": f"{update_form.updated_info.data}"
                }
            }
        )
        flash(f"{update_form.club_name.data} is updated successfully in the database.", "Success")
        return redirect(url_for("option"))
    return render_template("club_update.html", title="Club Entry form", update_form=update_form)

@app.route("/club/delete", methods = ["GET", "POST"])
def delete():
    delete_form = ClubDelete()
    if delete_form.validate_on_submit():
        db.clubs.delete_many({ "Club name": f"{delete_form.club_name.data}" })
        flash(f"{delete_form.club_name.data} is deleted successfully from the database.", "Success")
        return redirect(url_for("option"))
    return render_template("club_delete.html", title="Club Entry form", delete_form=delete_form)
 

if __name__ == "__main__":
    app.run(debug=True)
