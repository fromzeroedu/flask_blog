from flask_blog import app
from flask import request, render_template
from user.form import RegisterForm

@app.route('/login')
def login():
    return "Hello, Author!"

@app.route('/user/register', methods=('GET', 'POST'))
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('user/register.html', form=form)

@app.route('/success')
def success():
    return "Author registered!"
