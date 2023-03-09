from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField, IntegerField
from wtforms.validators import DataRequired
from datetime import datetime

class RegisterForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    surname = StringField("Surname", validators=[DataRequired()])
    age = IntegerField("Age", validators=[DataRequired()])
    position = StringField("position", validators=[DataRequired()])
    speciality = StringField("speciality", validators=[DataRequired()])
    address = StringField("Address", validators=[DataRequired()])
    email = EmailField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Submit")