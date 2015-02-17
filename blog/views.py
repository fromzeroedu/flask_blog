from flask_blog import app
from flask import render_template, redirect, flash, url_for, session
from blog.form import SetupForm, PostForm
from flask_blog import db
from user.models import User
from blog.models import Blog, Post, Category
from user.decorators import login_required, author_required
import bcrypt
from slugify import slugify

@app.route('/')
@app.route('/index')
def index():
    blog = Blog.query.first()
    posts = Post.query.order_by(Post.publish_date.desc())
    return render_template('blog/index.html', blog=blog, posts=posts)

@app.route('/admin')
@login_required
@author_required
def admin():
    posts = Post.query.order_by(Post.publish_date.desc())
    return render_template('blog/admin.html', posts=posts)

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
        if form.new_category.data:
            new_category = Category(form.new_category.data)
            db.session.add(new_category)
            db.session.flush()
            category = new_category
        else:
            category = form.category.data

        blog = Blog.query.first()
        author = User.query.filter_by(username=session['username']).first()
        title = form.title.data
        body = form.body.data
        slug = slugify(title)
        post = Post(blog, author, title, body, category, slug)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('article', slug=slug))
    return render_template('blog/post.html', form=form)

@app.route('/article/<slug>')
def article(slug):
    post = Post.query.filter_by(slug=slug).first_or_404()
    return render_template('blog/article.html', post=post)
