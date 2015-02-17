## Step #11

### List articles on admin and home page
- Get all posts in descending order in blog/views/admin
- Add post title and href on templates/admin.html
- Add a templates/blog/index.html
- Add the index function to blog/views
- Noticed an issue, need to pop is_author from session on user/views/logout
- Add login_required decoraton on top of author_required on blog/views/admin
- Add a footer with admin, login, logout on base.html
- Take out login_success and redirect to index on user/views/login
