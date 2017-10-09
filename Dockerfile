FROM python:3.6
RUN apt-get update && apt-get install -y \
  sudo \
  gettext \
  gcc \
  iotop \
  nano \
  netcat \
  tcpdump \
  mc \
  telnet \
  build-essential \
  python3-dev

RUN mkdir -p /usr/srv/walkonwater
WORKDIR /usr/srv/walkonwater

ADD . /usr/srv/walkonwater

RUN rm -rf walkonwater/settings/development.py
RUN pip install -U setuptools uwsgi
RUN pip install -r requirements.txt
RUN python manage.py collectstatic --noinput
COPY walkonwater.ini /etc/uwsgi/sites/

ENV DJANGO_SETTINGS_MODULE=walkonwater.settings
ENTRYPOINT ["uwsgi", "--module", "walkonwater.wsgi:application", "--static-map", "/static=/usr/srv/walkonwater/static"]

CMD ["--http", ":80"]