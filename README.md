## Step #0

### Create the initial folder setup
1. Add a settings.py file with basic stuff
1. Add requirements.txt
1. Added an ```__init__.py``` with Flask app
1. Added a manage.py as entry point
1. Added a home folder

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
docker run -id -p 5000:5000 -v /Users/jorge/flask_blog:/opt/flask_blog --name blog --link db:mysql flask_blog bash
docker exec -it blog bash
python manage.py runserver
```

### Check that it's running
Go to your boot2docker ip:5000 and you should see a "Hello World!"
