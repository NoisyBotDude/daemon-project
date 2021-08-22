from flask import Flask, render_template, flash, url_for, redirect
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["SECRET_KEY"] = "5791628bb0b13ce0c676dfde280ba245"

mongodb_client = PyMongo(app, uri="mongodb://localhost:27017/TUClubs")
db = mongodb_client.db

@app.route('/')
@app.route('/home')
def homePage():
    return render_template("home-page/home.html")

@app.route('/club')
def option():
    return render_template("club/form_option.html")

@app.route('/club/add', methods=["GET", "POST"])
def add():
    return render_template("club/club_add.html")

@app.route('/club/update', methods=["GET", "POST"])
def update():
    return render_template("club/club_update.html")

@app.route('/club/delete', methods=["GET", "POST"])
def delete():
    return render_template("club/club_delete.html")

if __name__ == '__main__':
    app.run(debug=True)
