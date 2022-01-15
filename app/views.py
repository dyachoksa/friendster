from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, login_required

from app import app
from app.models import User, users, get_user_by_email


@app.route("/")
def index():
    print(users)
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/terms")
def terms():
    return render_template("terms.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        user = get_user_by_email(email)
        if user is None:
            return render_template("login.html", error="User does not exist or password is wrong")
        
        if not user.verify_password(password):
            return render_template("login.html", error="User does not exist or password is wrong")

        login_user(user)

        return redirect(url_for("index"))

    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        user = User(email=request.form["email"], name=request.form["name"])
        user.set_password(request.form["password"])
        user.save()

        return redirect(url_for("index"))

    return render_template("register.html")


@app.route("/logout")
@login_required
def logout():
    logout_user()

    return redirect(url_for("index"))
