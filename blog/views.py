from flask_blog import app
from flask import render_template, redirect, flash, url_for, session
from blog.form import SetupForm, PostForm
from flask_blog import db
from user.models import User
from blog.models import Blog
from user.decorators import login_required, author_required
import bcrypt

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/admin')
@author_required
def admin():
    return render_template('blog/admin.html')

@app.route('/setup', methods=('GET', 'POST'))
def setup():
    blogs = Blog.query.count()
    if blogs:
        return redirect(url_for('admin'))
    form = SetupForm()
    if form.validate_on_submit():
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(form.password.data, salt)
        user = User(
            form.fullname.data,
            form.email.data,
            form.username.data,
            hashed_password,
            True
        )
        db.session.add(user)
        db.session.flush()
        if user.id:
            blog = Blog(form.name.data, user.id)
            db.session.add(blog)
            db.session.flush()
        else:
            db.session.rollback()
            error = "Error creating user"
        if user.id and blog.id:
            db.session.commit()
        else:
            db.session.rollback()
            error = "Error creating blog"
        flash('Blog created')
        return redirect('/admin')
    return render_template('blog/setup.html', form=form)

@app.route('/post', methods=('GET', 'POST'))
@author_required
def post():
    form = PostForm()
    if form.validate_on_submit():
        blog = Blog.query.first()
        author = User.query.get(session[''])
    return render_template('blog/post.html', form=form)
