from flask_blog import app
from flask import render_template, redirect, session, request, url_for
from user.form import RegisterForm, LoginForm
from user.models import User
from user.decorators import login_required
import bcrypt

@app.route('/login', methods=('GET', 'POST'))
def login():
    form = LoginForm()
    error = None

    if request.method == 'GET' and request.args.get('next'):
        session['next'] = request.args.get('next', None)

    if form.validate_on_submit():
        user = User.query.filter_by(
            username=form.username.data,
            ).first()
        if user:
            if bcrypt.hashpw(form.password.data, user.password) == user.password:
                session['username'] = user.username
                session['is_author'] = user.is_author
                if 'next' in session:
                    next = session.get('next')
                    session.pop('next')
                    return redirect(next)
                else:
                    return redirect(url_for('index'))
            else:
                error = "Incorrect password"
        else:
            error = "User not found"
    return render_template('user/login.html', form=form, error=error)

@app.route('/register', methods=('GET', 'POST'))
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('user/register.html', form=form)

@app.route('/logout')
def logout():
    session.pop('username')
    session.pop('is_author')
    return redirect(url_for('index'))

@app.route('/success')
def success():
    return "Author registered!"

@app.route('/login_success')
@login_required
def login_success():
    return "Author logged in!"
