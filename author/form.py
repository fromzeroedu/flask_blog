from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired

class RegisterForm(Form):
    username = StringField('Username', validators=[DataRequired()])
