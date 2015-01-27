## Step #0

### Create the initial folder setup
1. Everything contained in the app folder.
1. Added an ```__init__.py``` with Flask app
1. Added a manage.py as entry point

### Start the main db:
```
docker run --name db -e MYSQL_ROOT_PASSWORD=test -d -p 3306:3306 mariadb
```

### Tie the web app with the db app

Regenerate the container with the new requirements.txt (flask-mysql)

```
docker build -t flask_blog .
```

Run the web container as (note for now you can only mount /Users folders)
NO MORE virtualenv:
```
docker run -d -p 5000:5000 -v /Users/jorge/flask_blog:/opt/flask_blog --name blog --link db:mysql flask_blog
```

### Check that it's running
Go to your boot2docker ip:5000 and you should see a "Hello World!Â"
