from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired

class Register(Form):
    username = StringField('name', validators=[DataRequired()])
