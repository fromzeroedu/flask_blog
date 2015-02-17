## Step #13

### Add a photo to the post
- Add flask-uploads to requirements.txt and install on container
- Add UPLOADED_PHOTOS_DEST to settings
- Add upload_set config to __init__
- Add upload to blog/views/post (NOTE: Add request to flask)
- Add filefield to blog/forms
- Add image to blog/models/post and do a migrate
- Add flash template to article view (for error uploads)
