FROM ubuntu

RUN apt-get update

RUN apt-get install python3 -y

RUN apt-get install python3-pip -y

RUN pip3 install django

RUN pip3 install gunicorn

WORKDIR /djangoapp

COPY . /djangoapp

# EXPOSE 8000

# CMD exec python3 manage.py runserver 0.0.0.0:8000

# CMD exec gunicorn --bind 0.0.0.0:8000 mysite.wsgi --workers 3