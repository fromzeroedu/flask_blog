## Step #15

### Testing
- Add {% include '_flashmessages.html' %} to templates/user/login and templates/blog/index
- Add a flash "user logged in" in user/views/login #L24, "user logged out" in #L48 and import flash at the top
- Change the blog/views/setup redirect on #L61 to go to /index, otherwise there's a weird issue
- Update the templates/user/register.html to include an email
- Add the actual database registration on user/views/register, import db at the top
- Create a tests.py

Run using python tests.py (inside the container)
