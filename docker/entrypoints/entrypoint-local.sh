#!/usr/bin/env bash

sleep 10
/rsc/wait-for-it.sh -h naturitas_db -p 3306 -t 120
python manage.py makemigrations
python manage.py migrate --noinput

python manage.py deploy_v0_0_1

python manage.py runserver 0.0.0.0:8000