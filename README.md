## Step #6

### Secure passwords
Passwords should be stored as hashes so that if a hacker gets access, he won't be able to decode. We need to install a few packages.
- Add py-bcrypt and install
- Add the salting function to blog/views/setup
- On migrations/env.py add compare_type=True in the run_migrations_online, context_configure
- Change the password length to 60
- Do ```python manage.py db migrate```
- Check the new file generated on migrations/versions
- Do ```python manage.py db upgrade```
