## Step #9

### Add an "author required" decorator
- Change the admin @login_required to @author_required and take out the auto-setup and add blog check to /setup

### Adding a Blog Post form and page
- Add the PostForm to form.py
- Create the function on the blog/view
- Change the init on the blog/models post category to category_id
- Add python-slugify to requirements
