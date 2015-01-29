from flask_blog import app
from flask import request, render_template

@app.route('/login')
def login():
    return "Hello, Author!"

@app.route('/author/register')
def register():
    return render_template('author/register.html')
