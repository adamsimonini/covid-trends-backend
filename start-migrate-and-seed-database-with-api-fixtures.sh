#!/bin/bash

# Parses out the current working directory
WORKING_DIR=$(basename "$PWD")

docker compose up -d
sleep 0
docker compose exec web python manage.py makemigrations --noinput
sleep 0
docker compose exec web python manage.py migrate -
-noinput

# Creates the admin user
# username: admin@g.com , password: 123
sleep 1
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin@g.com', '123')" | docker compose exec web python manage.py shell

# Band-aid for error found on the container, error output found below
# ValueError: Dependency on app with no migrations: api
sleep 1
docker container restart ${WORKING_DIR}-web-1