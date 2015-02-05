## Step #6

### Secure passwords
Passwords should be stored as hashes so that if a hacker gets access, he won't be able to decode. We need to install a few packages.
- Add py-bcrypt and install
- Add the salting function to blog/views/setup
- On migrations/env.py add compare_type=True in the run_migrations_online, context_configure ([explanation here](http://www.reddit.com/r/flask/comments/1glejl/alembic_autogenerate_column_changes/cale9o0))
- Change the password length to 60
- Do ```python manage.py db migrate```
- Check the new file generated on migrations/versions
- Do ```python manage.py db upgrade```
- Go to /setup, and register. If you see the password in the db it's now a hash
- Add login functionality using hash to member/views/login (and add import bcrypt)
- Add logout functionality on user/views
- Add a temporary "Welcome, username - logout" on /admin
