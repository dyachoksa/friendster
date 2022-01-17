from flask import render_template, request, redirect, url_for, flash
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
    next = request.args.get('next')

    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        user = get_user_by_email(email)
        if user is None:
            return render_template("login.html", error="User does not exist or password is wrong")
        
        if not user.verify_password(password):
            return render_template("login.html", error="User does not exist or password is wrong")

        login_user(user)

        flash("Welcome back! You successfully signed in.", "success")

        next = request.form.get('next')

        return redirect(next or url_for("index"))

    return render_template("login.html", next=next)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        user = User(email=request.form["email"], name=request.form["name"])
        user.set_password(request.form["password"])
        user.save()

        login_page_url = url_for('login')

        flash(f"Welcome! You successfully registered on our site. Please <a href='{login_page_url}'>login</a> to continue.", "success")

        return redirect(url_for("index"))

    return render_template("register.html")


@app.route("/profile")
@login_required
def profile():
    return render_template("profile.html")


@app.route("/logout")
@login_required
def logout():
    logout_user()

    flash("Goodbay! We hope to see you soon again.", "success")

    return redirect(url_for("index"))
