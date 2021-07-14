#!/bin/sh

while ! nc -z 3306-mysql 3306 ; do
    echo "Waiting for the MySQL Server"
    sleep 3
done

python manage.py runserver 0.0.0.0:8002