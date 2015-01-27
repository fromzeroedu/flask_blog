#
# First Flask App Dockerfile
#
#

# Pull base image.
FROM centos:7.0.1406

# Build commands
RUN yum install -y python-setuptools mysql-connector-python mysql-devel gcc python-devel
RUN easy_install pip
RUN mkdir /opt/flask-blog
WORKDIR /opt/flask-blog
ADD requirements.txt /opt/flask-blog/
RUN pip install -r requirements.txt
ADD . /opt/flask-blog

# Define working directory.
WORKDIR /opt/flask-blog

# Define default command.
CMD ["python", "manage.py", "runserver"]

# Expose ports.
EXPOSE 5000
