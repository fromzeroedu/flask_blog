## Step #9

### Add an "author required" decorator
- Change the admin @login_required to @author_required and take out the auto-setup and add blog check to /setup

### Adding a Blog Post form and page
- Add the PostForm to form.py
- Create the function on the blog/view

### Adding Markdown
- Add flask-markdown in requirements.txt and pip install in container
- Add Markdown(app) to __init__.py

### Create a post view function
- Add the post view to blog/views
- Add the markdown renderer on templates/blog/article.html
