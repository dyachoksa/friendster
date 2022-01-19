# Friendster Application
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy


application_name = "Friendster"
version = "1.0"

welcome_message = "Welcome to the {0}. Version v{1}!".format(application_name, version)

app = Flask(__name__)

# store it in the secure place, like system eviroment variables
app.config["SECRET_KEY"] = "4676f265c9e6f6c6c2dce5ea7f3975aebacd0b446b79083eb3d263752800e20b"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.sqlite"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Create an instance of the datatbase extension 
db = SQLAlchemy(app)

# Create an instance of Flask-Login extension
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


from app.models import User


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()


from app import views

# db.create_all()
