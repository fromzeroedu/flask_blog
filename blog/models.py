from flask_blog import db
from datetime import datetime

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    admin = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, name, admin):
        self.name = name
        self.admin = admin

    def __repr__(self):
        return '<Name %r>' % self.name

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    blog = db.Column(db.Integer, db.ForeignKey('blog.id'))
    author = db.Column(db.Integer, db.ForeignKey('user.id'))
    title = db.Column(db.String(80))
    body = db.Column(db.Text)
    publish_date = db.Column(db.DateTime)
    live = db.Column(db.Boolean)

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship('Category',
        backref=db.backref('posts', lazy='dynamic'))

    def __init__(self, blog, author, title, body, category, pub_date=None, live=True):
            self.blog = blog
            self.author = author
            self.title = title
            self.body = body
            self.category = category
            if pub_date is None:
                pub_date = datetime.utcnow()
            self.live = live

    def __repr__(self):
        return '<Post %r>' % self.title


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Category %r>' % self.name
