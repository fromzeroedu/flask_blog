## Step #1

### Docker management
1. Make sure to tail your logs via docker logs blog
1. If you produce an error, the docker container will stop. Correct the error and then do ```docker start blog```

### Why an author module?
We want to split the application in different components and group all the related functions and models in those folders.

### Create the author module and database
1. Add author init and views
1. Add author model
1. Add author.views to main ```__init__```

### Add the database
```
docker exec -it blog bash
python
import sqlalchemy
engine = sqlalchemy.create_engine("mysql://root:test@mysql")
conn = engine.connect()
conn.execute("commit")
conn.execute("create database blog")
conn.close()

```

### Test the database connection
```
docker exec -it blog bash
python
import os, sys
sys.path.append(os.path.abspath(os.path.join('/opt/flask_blog', '..')))
from flask_blog import db
from author.models import Author
db.create_all()
author = Author('admin', 'admin@example.com')
db.session.add(author)
db.session.commit()
author.id
get_admin = Author.query.filter_by(username='admin').first()
get_admin.id
db.session.delete(author)
db.session.commit()
```
