# Friendster Application
from flask import Flask
from flask_login import LoginManager

from app.models import get_user_by_email

application_name = "Friendster"
version = "1.0"

welcome_message = "Welcome to the {0}. Version v{1}!".format(application_name, version)

app = Flask(__name__)

# store it in the secure place, like system eviroment variables
app.config["SECRET_KEY"] = "4676f265c9e6f6c6c2dce5ea7f3975aebacd0b446b79083eb3d263752800e20b"

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


@login_manager.user_loader
def load_user(user_id):
    return get_user_by_email(user_id)


from app import views
