from ast import Pass
from unicodedata import name
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, Email, Length


class RegistrationForm(FlaskForm):
    email = EmailField("Email", validators=[DataRequired(), Email()])
    name = StringField("Name", validators=[DataRequired(), Length(max=50, min=3)])
    password = PasswordField("Password", validators=[DataRequired()])


class LoginForm(FlaskForm):
    email = EmailField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])


class PostForm(FlaskForm):
    content = TextAreaField("Message", validators=[DataRequired(), Length(min=5, max=600)])
