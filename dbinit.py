# Set the path
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import sqlalchemy

from flask_blog import app, db
from user.models import *
from blog.models import *

# If you want to create the database and tables
# run the code below
db_uri = 'mysql://%s:%s@mysql:3306/' % (app.config['DB_USERNAME'], app.config['DB_PASSWORD'])
engine = sqlalchemy.create_engine(db_uri)
conn = engine.connect()
conn.execute("commit")
conn.execute("create database "  + app.config['BLOG_DATABASE_NAME'])
db.create_all()

# If you want to drop the database
#conn.execute("drop database "  + app.config['BLOG_DATABASE_NAME'])

conn.close()
