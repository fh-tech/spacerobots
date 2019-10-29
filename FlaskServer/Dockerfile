FROM python:3.7-slim

RUN useradd -ms /bin/bash flaskapp

RUN apt-get clean \
    && apt-get -y update

RUN apt-get -y install python3-dev \
    && apt-get -y install build-essential

COPY ./requirements.txt /srv/flask-app/requirements.txt
WORKDIR /srv/flask-app
RUN pip install -r requirements.txt --src /usr/local/src


COPY ./app /srv/flask-app
COPY ./uwsgi.ini /srv/flask-app

RUN chown -R flaskapp /srv

USER flaskapp
CMD ["uwsgi", "--ini", "uwsgi.ini"]
