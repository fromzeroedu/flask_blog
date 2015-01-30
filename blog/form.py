from flask_wtf import Form
from wtforms import validators, StringField, PasswordField
from wtforms.fields.html5 import EmailField

class SetupForm(Form):
    name = StringField('Blog Name', [
            validators.Required(),
            validators.Length(max=80)
        ])
    fullname = StringField('Full Name', [validators.Required()])
    email = EmailField('Email address', [validators.DataRequired(), validators.Email()])
    username = StringField('Username', [
            validators.Required(),
            validators.Length(min=4, max=25)
        ])
    password = PasswordField('New Password', [
            validators.Required(),
            validators.EqualTo('confirm', message='Passwords must match'),
            validators.Length(min=4, max=80)
        ])
    confirm = PasswordField('Repeat Password')
