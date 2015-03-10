## Step #15

### Testing
- Add {% include '_flashmessages.html' %} to templates/user/login and templates/blog/index
- Add a flash "user logged in" in user/views/login #L24 and import flash at the top
- Change the blog/views/setup redirect on #L61 to go to /index, otherwise there's a weird issue
- Create a tests.py

Run using python tests.py (inside the container)
