#!/usr/bin/env bash

sleep 30
python manage.py makemigrations
python manage.py migrate --noinput

python manage.py deploy_v0_0_1

python manage.py runserver 0.0.0.0:8000