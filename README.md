## Step #15

### Testing
- "Something that is untested is broken."
- Top concepts in testing
   - Don't test things that are external to your application, for example sessions are set?
   - Write tests that cover all possible uses, including edge cases. Be creative!
   - Check for the 1, 2, N scenarios. For example what happens if you have an API that receives multiple entries and you test passing one item in the call, and then 4, with #3 being completely garbage
   - Look into TDD (Test-driven-development), i.e. create the test as you write the code

### Steps
- Add {% include '_flashmessages.html' %} to templates/user/login and templates/blog/index
- Add a flash "user <user> logged in" in user/views/login #L24, "user logged out" in #L48 and import flash at the top
- Change the blog/views/setup redirect on #L61 to go to /index, otherwise there's a weird issue
- Update the templates/user/register.html to include an email
- Add the actual database registration on user/views/register, import db at the top
- Create a tests.py
- Found an issue with the is_author decorator! Need to test if it's False! Thanks, testing!

Run using python tests.py (inside the container)
