from flask_blog import app
from flask import render_template, redirect, flash, url_for
from blog.form import SetupForm
from flask_blog import db
from user.models import User
from blog.models import Blog

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/admin')
def admin():
    blogs = Blog.query.count()
    if blogs == 0:
        return redirect(url_for('setup'))
    return render_template('blog/admin.html')

@app.route('/setup', methods=('GET', 'POST'))
def setup():
    form = SetupForm()
    if form.validate_on_submit():
        user = User(
            form.fullname.data,
            form.email.data,
            form.username.data,
            form.password.data,
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
