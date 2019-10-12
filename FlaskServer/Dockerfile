FROM python:3.7-slim

RUN apt-get clean \
    && apt-get -y update

RUN apt-get -y install python3-dev \
    && apt-get -y install build-essential

COPY ./app /srv/flask-app
COPY ./requirements.txt /srv/flask-app
COPY ./uwsgi.ini /srv/flask-app

WORKDIR /srv/flask-app

RUN pip install -r requirements.txt --src /usr/local/src

CMD ["uwsgi", "--ini", "uwsgi.ini"]