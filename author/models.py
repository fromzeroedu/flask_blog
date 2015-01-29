from flask_blog import db

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(30))
    is_admin = db.Column(db.Boolean)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<Author %r>' % self.username
