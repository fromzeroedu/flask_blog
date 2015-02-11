## Step #8

### Creating the Post module
- Add a function post on the blog/view
- Create the blog post model and the blog category model
   - NOTE: Columns are named 'user_id' and 'blog_id', otherwise the ORM fails if we pass the user as the parameter on the post
- Add the db.backref to models.user
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

user = User.query.first()
blog = Blog.query.first()
category = Category.query.first()
post = Post(blog, user, 'Python is cool!', 'This is why Python is cool.', category)
db.session.add(post)
db.session.commit()

category.posts.all()
user.posts.all()
blog.posts.all()
```

Let's delete the test records:
```
Post.query.delete()
Category.query.delete()
db.session.commit()
```
