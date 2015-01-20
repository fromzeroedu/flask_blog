### Step #0

Create the initial folder setup

## MySQL Setup

### Start boot2docker
```
boot2docker start
```

### Export environment variables
```
export DOCKER_HOST=tcp://192.168.59.103:2376
export DOCKER_CERT_PATH=/Users/jorge/.boot2docker/certs/boot2docker-vm
export DOCKER_TLS_VERIFY=1
```

### Start the main db:
```
docker run --name db -e MYSQL_ROOT_PASSWORD=test -d -p 3306:3306 mariadb
```

## Tie the web app with the db app

Regenerate the container with the new requirements.txt (flask-mysql)

```
docker build -t flask-blog .
```

Run the web container as (note for now you can only mount /Users folders):
```
docker run -d -p 5000:5000 -v /Users/jorge/projects/flask-blog:/opt/flask-blog --name web --link db:mysql flask-blog
```
