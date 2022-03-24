#!/bin/bash

docker compose exec web python manage.py makemigrations --noinput
sleep 0
docker compose exec web python manage.py migrate --noinput
sleep 0
docker compose exec web python manage.py loaddata api_fixture
sleep 0