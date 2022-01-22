import datetime as dt

from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required

from app import app, db
from app.forms import RegistrationForm, LoginForm
from app.models import User


@app.route("/")
def index():
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
    form = LoginForm()

    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        user = User.query.filter_by(email=email).first()
        if user is None:
            return render_template("login.html", form=form, error="User does not exist or password is wrong")
        
        if not user.verify_password(password):
            return render_template("login.html", form=form, error="User does not exist or password is wrong")

        login_user(user)

        user.last_logged_at = dt.datetime.utcnow()
        db.session.commit()

        flash("Welcome back! You successfully signed in.", "success")

        next = request.form.get('next')

        return redirect(next or url_for("index"))

    return render_template("login.html", form=form, next=next)


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(email=form.email.data, name=form.name.data)
        user.set_password(form.password.data)
        
        db.session.add(user)
        db.session.commit()

        login_page_url = url_for('login')

        flash(f"Welcome! You successfully registered on our site. Please <a href='{login_page_url}'>login</a> to continue.", "success")

        return redirect(url_for("index"))

    return render_template("register.html", form=form)


@app.route("/profile")
@login_required
def profile():
    return render_template("profile.html")


@app.route("/users")
@login_required
def users_list():
    users = User.query.all()
    return render_template("users_list.html", users=users)


@app.route("/logout")
@login_required
def logout():
    logout_user()

    flash("Goodbay! We hope to see you soon again.", "success")

    return redirect(url_for("index"))
