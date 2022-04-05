#!/bin/bash

docker compose up -d
sleep 0
docker compose exec web python manage.py makemigrations --noinput
sleep 0
docker compose exec web python manage.py migrate --noinput
sleep 0
docker compose exec web python manage.py loaddata disease geo