## Step #2

### Add flask-wtf to requirements and rebuild
```
docker exec -it blog bash
pip install flask-wtf
```

### Create an /author/register form with WTF Forms
First add the route on the views (/author/register)
Create the templates/author folder

### If table doesn't exist, add the database
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
sys.path.append(os.path.abspath('/opt'))
sys.path.append(os.path.abspath('/opt/flask_blog'))
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
