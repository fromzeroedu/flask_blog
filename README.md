## Step #2

### Add flask-wtf to requirements and rebuild
```
pip install -r requirements.txt
```

### Initialize Database
Modify settings.py with separate credential variables
Create dbinit.py and run it

### Setup jquery and Bootstrap
Create a base.html and add Twitter bootstrap and jquery to static.
- Get http://jquery.com/download/
- Get https://github.com/twbs/bootstrap/releases/download/v3.3.2/bootstrap-3.3.2-dist.zip
- Move to static css, javascript

### Create a /user/register form with WTF Forms
First add the route on the views (/user/register).
Create the templates/user folder.
Create the _formhelpers.html
Create the register form.
Create the register view.
