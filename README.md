## Step #4

### Implement a login function and logged in decorator
- Create the login page
  - Login form
  - Login html
  - login_success temporary page
  - Add db check of credentials
  - Add user to the session
  - Add error message to login page

- Create a login decorator
  - Add user decorators.py
  - Import user.decorators login_required to user and add to login_success
  - Add next query param to session
  - Add check if next session to redirect there
  - Add login_required decorator to /admin
