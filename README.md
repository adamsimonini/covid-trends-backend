# **COVIDTrends Backend in Python, Postgres, Flask, & Docker**

## **What and why**

This is the backend part of a fullstack application. Ideally this application will serve as the database and API for COIVDTrends, a Canadian application dedicated to showing Canadians geographically relevant COVID-19 data.

## **Technology**

- Python along with Flask are used to communicate with the database and generate an API for the client to query the database.
- Postgres is used as the database. With Postgres our API can make SQL queries on the data.
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

4. The API, postgres database, and pgAdmin (Postgres GUI) should now be running. Visit pgAdmin by visiting [localhost:5433/browser/](http://localhost:5433/browser/)

## **Retrospective**

1. **Did you choose to use an ORM or raw SQL? Why?**
   I am aiming to use raw SQL within Flask. I hate the limited documentation of ORMs, along with the abstrction that ORMs produce. They prevent me from solidifying my understand of SQL. I would rather struggle with SQL and move slowly, than move quickly but be doomed to reading obscure forum posts on troubleshooting ORM issues.

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

Example of a valid post request:

```
{
	"name":"Adrian",
        "sex":"male",
	"user_id": 3,
	"city_id": 3
}
```
-->

## **Database Dump**

A database dump created by pg_dump can be found in `./data` -->

## **Insomnia API Endpoint Export**

tbd

## **Entity Relationship Diagrams**

tbd

# **Limitations & Shortcomings**

# **Successes**

\*(Dev) denotes work done for the benefit of the development environment

- [✔️] utilized Flask's "blueprint" functionarlity to splitup my API routes into multiple files
- [✔️] (Dev) Docker Compose yaml now creates 3 containers on a single network: api (backend code), pg (postgres), and pgadmin
- [✔️] (Dev) Docker Compose yaml now generates the postgres database from raw SQL durion container build
- [✔️] (Dev) The API ports for the development host machine and the container are correctly mapped to 8000, so the API returns JSON objects

# **Notes**
