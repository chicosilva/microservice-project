FROM python:3.8.3-alpine
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add --no-cache mariadb-dev

RUN apk add --no-cache openssl bash mysql-client nodejs npm alpine-sdk autoconf librdkafka-dev vim nginx openrc 
RUN apk add --no-cache bash  python3-dev build-base

RUN mkdir -p /run/nginx && \
    echo "pid /run/nginx.pid;" >> /etc/nginx/nginx.conf

WORKDIR /var/www

RUN pip install --upgrade pip 
RUN pip install --upgrade setuptools
RUN pip install mysqlclient kafka-python lz4 crc32c django-apscheduler Faker


RUN apk del build-deps
COPY ./requirements.txt /var/www
COPY ./wait.sh /var/www
RUN pip install -r requirements.txt
RUN pip install kafka-python

RUN rm -rf /var/www/html
RUN ["chmod", "+x", "./wait.sh"]

RUN rm /etc/nginx/conf.d/default.conf
COPY .docker/nginx/nginx.conf /etc/nginx/conf.d

EXPOSE 8000
