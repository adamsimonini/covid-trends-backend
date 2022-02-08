# **COVIDTrends Backend in Python, Postgres, Django, & Docker**

## **What and why**

This is the backend part of a fullstack application. Ideally this application will serve as the database and API for COIVDTrends, a Canadian application dedicated to showing Canadians geographically relevant COVID-19 data.

## **Technology**

- Python along with Flask are used to communicate with the database and generate an API for the client to query the database.
- Postgres is used as the database. With Postgres our API can make SQL queries on the data.
- Django acts as an all-in-one framework for API creation. It includes an ORM, as well as routing.
- Docker will be used to containerize both the backend application, as well as the database. This will help with development and deployment on Windows Azure.

## **Steps to Replicate Dev Environment**

1. Clone this repo
2. Download Docker Desktop for [Windows](https://hub.docker.com/editions/community/docker-ce-desktop-windows/) or [Mac](https://docs.docker.com/docker-for-mac/install/)

- **Windows Install**

  ![win install](images/windows-docker-install.png)

  [Download WSL2 msi here](https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi)

- **Mac Install**

  ![mac install](images/mac-docker-install.png)

3. On the root directory (where the docker-compose.yml file resides), type "docker compose up -d" into the terminal. This will take a while the first time, since Docker is downloading all required images from DockerHub. Our docker-compose.yml will start multiple containers and place them on the same network. Once completed, you can input "docker ps" into the terminal to see the running containers:

- ![confirm containers are running](images/docker-ps-example.png)

4. Ensure you have a .env file on the root directory, which includes the appropriate values for the following keys (you may ask a colleague for their .env file, as the values are not to be shared on github):

```
# dev environment
DEBUG=True

# database settings
DB_NAME=???
DB_USER=???
DB_PASSWORD=???
DB_HOST=???
DB_PORT=???

SECRET_KEY=???

```

5. All Django apps are dependent on a set of default tables to store users, groups, session information, migrations logs, etc. These default tables are part of the built-in Django framework and are required for a Django website to function properly. To generate these tables, make sure that your Docker Compose containers are all running, then open a bash terminal and run the following two commands:

```
docker compose exec web python manage.py makemigrations --noinput
docker compose exec web python manage.py migrate --noinput
```

6. To seed the database with randomly generated values that will respect the typecasting on the model definitions, we're using a small python package called [django-seed](https://github.com/Brobin/django-seed). After the models have been migrated into the database (see step 7), you can seed each resulting table with 15 records via the following command:

```
docker compose exec web python manage.py seed api --number=15
```

7. The API, postgres database, and pgAdmin (Postgres GUI) should now be running each in their own containers. Visit pgAdmin by visiting [localhost:5433/browser/](http://localhost:5433/browser/)

8. Due to Docker bind mounting specified in the docker-compose.yml, there is no need to remake Docker images or restart the server during development. Changes to API endpoints and routing within ./app should be reflected automatically.

## **Testing**

From ./app, testing can be done with the pytest unit testing package via the following command:

```
pytest -v
```

## **Q&A**

1. **Did you choose to use an ORM or raw SQL? Why?**
   Flask was initially chosen as a microserver framework. I also wished to avoid ORMs with Flask. Quickly, after doing some research, it became apparent that avoid ORMs was not going to be possible, and that I would have to embrace them. In order to get better documentation and community support, I decided to change to Django. It's more opinionated than Flask, which means documentation is less fragmented.

2. **What future improvements are in store, if any?**
   n/a

## **API Endpoints Reference**

**Dev base_url: localhost:5000**

### **Endpoint Grouping One**

| METHOD | NAME                  | PATH                                                              | RESULT                                                                      |
| ------ | --------------------- | ----------------------------------------------------------------- | --------------------------------------------------------------------------- |
| GET    | all health regions    | base_url/health-regions                                           | returns all recrods from the health_regions table                           |
| GET    | single health region  | base_url/health-regions/<span style="color:lightgreen">{id}<span> | returns single record based on id parameter                                 |
| Get    | health regions by fsa | base_url/fsa/<span style="color:lightgreen">{id}<span>            | return an array of one or more health regions belonging to the provided fsa |

<!-- Example of a valid get request:

```
{
  "email":"a@g.com",
  "password":"@my_secret_password_123",
  "phone_number":"9991234563",
  "birthday":"1999-06-06"
}
```

### **Endpoint Grouping Two**

| METHOD | NAME                    | PATH                                                          | RESULT                                           |
| ------ | ----------------------- | ------------------------------------------------------------- | ------------------------------------------------ |
| GET    | get all companions      | base_url/companions                                           | returns all recrods from the companion table     |
| GET    | get single companion    | base_url/companions/<span style="color:lightgreen">{id}<span> | returns single record based on id parameter      |
| POST   | create single companion | base_url/companions                                           | creates a new record based on valid JSON request |
| DELETE | delete single companion | base_url/companions/<span style="color:lightgreen">{id}<span> | deletes a record based on id parameter           |

Example of a valid post request:

```
{
	"name":"Sabrina",
        "sex":"female",
	"user_id": 4,
	"sexual_orientation_id": 1,
	"city_id": 1
}
```

### **Endpoint Grouping Three**

| METHOD | NAME                 | PATH                                                      | RESULT                                           |
| ------ | -------------------- | --------------------------------------------------------- | ------------------------------------------------ |
| GET    | get all patrons      | base_url/patron                                           | returns all recrods from the patron table        |
| GET    | get single patron    | base_url/patron/<span style="color:lightgreen">{id}<span> | returns single record based on id parameter      |
| POST   | create single patron | base_url/patron                                           | creates a new record based on valid JSON request |
| DELETE | delete single patron | base_url/patron/<span style="color:lightgreen">{id}<span> | deletes a record based on id parameter           |

-->

## **Postman API Endpoint Export**

tbd

## **Entity Relationship Diagrams**

database documentation (including ERDs), queries for development, and database initialize SQL can be found here: ./data/schema

# **Limitations & Shortcomings**

# **Successes**

\*(Dev) denotes work done for the benefit of the development environment

- ✅ (Dev) Docker Compose yml creates 3 containers on a single network: api (backend code), pg (postgres), and pgadmin
- ✅ (Dev) Docker Compose yml generates the postgres database from raw SQL durion container build
- ✅ (Dev) Docker Compose yml has volumes setup correctly to enable hot reloading of server files (i.e., no rebuilding of images required)
- ✅ (Dev) The API ports for the development host machine and the container are correctly mapped to 8000, so the API returns JSON objects
- ✅ (Dev) First ORM models produced and first database migrations made
- ✅ (Dev) First true GET request made to database for health regions
- ✅ (Dev) Added django-seed library for auto-populating models

# **Troubleshooting**

- migration: if you have problems with migration, use "docker compose down" to destroy all running containers, then delete the migrations within ./app/api/migrations, but leave **init**.py

- unkown issues: before troubleshooting a mysterious issue, it might be usefull to fully destroy all elements of this app on Docker and re-initialize the containers. While the containers are running, enter the following into terminal:

```
docker compose down --rmi all --volumes
```
