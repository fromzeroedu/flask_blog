from flask_blog import db

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    fullname = db.Column(db.String(80))
    password = db.Column(db.String(30))
    is_admin = db.Column(db.Boolean)

    def __init__(self, username, fullname, password, is_admin):
        self.username = username
        self.fullname = fullname
        self.password = password
        self.is_admin = is_admin

    def __repr__(self):
        return '<Author %r>' % self.username
