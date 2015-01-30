from flask_blog import db

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    admin = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, name, admin):
        self.name = name
        self.admin = admin

    def __repr__(self):
        return '<Name %r>' % self.name
