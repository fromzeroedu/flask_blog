## Step #7

### Create an author check on admin
- Rework users code on login to use first() and single user instead of users
- Add is_author to the session on login so we can check on it
- Add a check of is_author on admin and return a 403 (not authorized) if not (import abort)
- Set the user's is_author to False to test:
```
>>> from user.models import *
>>> user = User.query.first()
>>> user
<Author u'jorge'>
>>> user.is_author
True
>>> user.is_author = False
>>> db.session.commit()
```
