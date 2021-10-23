from flask import Blueprint, render_template, flash, url_for, redirect, request, session
from werkzeug.security import generate_password_hash, check_password_hash
from club_app.database.database import AdminDataBase
from flask_session import Session


def create_blueprint():
    admin_auth = Blueprint("admin_auth", __name__, url_prefix="/admin")

    @admin_auth.route("/")
    def admin_home():
        return render_template("/admin/index.html")

    @admin_auth.route("/register", methods=["GET", "POST"])
    def admin_register():
        if request.method == "POST":
            if AdminDataBase.is_registered(request.form.get("email")):
                flash("You've already signed up with that email, log in instead!")
                return redirect(url_for("admin_auth.admin_login"))
            else:
                hash_and_salted_password = generate_password_hash(
                    request.form.get("password"),
                    method="pbkdf2:sha256",
                    salt_length=8
                )
                AdminDataBase.add_admin(
                    email=request.form.get("email"),
                    name=request.form.get("name"),
                    password=hash_and_salted_password
                )
                return redirect(url_for("admin.option"))
        return render_template("/admin/register.html")

    @admin_auth.route("/login", methods=["GET", "POST"])
    def admin_login():
        if request.method == "POST":
            email = request.form.get("email")
            password = request.form.get("password")
            admin_data = AdminDataBase.find_admin(email, password)
            if admin_data:
                if check_password_hash(admin_data["password"], password) == True:
                    session["name"] = admin_data["name"]
                    return redirect(url_for("admin.option"))
            else:
                flash("Username or Password incorrect!!!")
                return redirect(url_for("admin_auth.admin_login"))
        return render_template("/admin/login.html")

    @admin_auth.route("/logout")
    def admin_logout():
        session["name"] = None
        return redirect(url_for("admin_auth.admin_home"))

    return admin_auth