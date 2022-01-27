From ./app, you can run the app without the db or pgAdmin with this command:

```
python manage.py runserver 0.0.0.0:8000 // this command needs to be the execution command found in either the ./app/Dockerfile and ./docker-compose.yml
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
docker run -d --rm -p 8000:8000 31999f1fdeb8
```

To run all three - API app, Postgres server, and pgAdmin - containers, run the following command at the root directory:

```
docker compose up -d
```
