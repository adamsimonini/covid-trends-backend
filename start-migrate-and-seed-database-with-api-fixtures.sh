#!/bin/bash

docker compose up -d
sleep 3
docker compose exec web python manage.py makemigrations --noinput
sleep 3
docker compose exec web python manage.py migrate --noinput
sleep 3
docker compose exec web python manage.py loaddata api_fixture