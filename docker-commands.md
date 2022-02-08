From ./app, you can run the app without the db or pgAdmin with this command:

```
python manage.py runserver 0.0.0.0:8000 // this command needs to be the execution command found in either the ./app/Dockerfile and ./docker-compose.yml. You can also use it to run the API without docker.
```

If you need to build an image for the app specifically, outside of docker compose, you can do so with the Docker CLI form ./app with the following command:

```
docker build -t pht .
```

Confirm the image is installed and get its ID via the Docker CLI:

```
docker images
```

How to run the image alone, without docker-compose.ylm:

```
docker run -d --rm -p 8000:8000 {image ID}
```

To run all three - API app, Postgres server, and pgAdmin - containers, run the following command at the root directory:

<!--  -->

```
docker compose up -d // must be run from root, as it relies on the .env there
```

Remove the docker containers, remove all images, and remove all volumes:

```
docker compose down --rmi all --volumes
```

Remove all containers and cached images/containers

```
docker system prune
```

```

# dev environment
DEBUG=True

# Database Settings
DB_NAME=public_health_trends
DB_USER={postgres admin name}
DB_PASSWORD={password for admin}
DB_HOST=127.0.0.1
DB_PORT={port postgres is running on}
DJANGO_SECRET_KEY={your django secret}

# Hosting
ALLOWED_HOSTS=.localhost, .herokuapp.com
}
```

Troubleshooting

```
After starting and stopping containers, there seems to be some corruption with Docker and CLI commands and pg_container. Sometimes after starting the pg_container, the database fails to initalize. The logs for thef pg_container will state "PostgreSQL database already found. Skipping initialization". If the database is not initalizing on docker compose up -d, consider exiting the terminal and starting a new one. Sometimes this seems to fix the issue for reasons unknown.
```
