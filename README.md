## Step #8

### Creating the Post module
- Add a function post on the blog/view
- Create the blog post model and the blog category model
- Do the migration:
```
python manage.py db migrate
python manage.py db upgrade
```
- Let's create some posts:
```
python manage.py shell
from user.models import *
from blog.models import *
category = Category('Python')
db.session.add(category)
db.session.commit()
user = User.query.first()
blog = Blog.query.first()
post = Post(blog, user, 'Python is cool!', 'This is why Python is cool.', category)
db.session.add(post)
db.session.commit()
```
