## Step #13

### Add a photo to the post
- Add flask-uploads to requirements.txt and install on container
- Add UPLOADED_IMAGES_DEST and UPLOADED_IMAGES_URL to settings
- Add upload_set config to __init__
- Add upload to blog/views/post (NOTE: Add request to flask)
- Add filefield to blog/forms
- Add image to blog/models/post and do a migrate
- Add a property to the blog/models/post for imgsrc
- Add an image renderer on templates/blog/article
- Add image on post list templates/blog/index (make sure to add class row)
- Add image on admin list templates/blog/admin (make sure to add class row)
- Create flash messages template
- Add flash template to article view (for error uploads)
- Add New Article link on admin
