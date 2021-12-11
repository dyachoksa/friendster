# Friendster Application
from flask import Flask

application_name = "Friendster"
version = "1.0"

welcome_message = "Welcome to the {0}. Version v{1}!".format(application_name, version)

app = Flask(__name__)

from app import views
