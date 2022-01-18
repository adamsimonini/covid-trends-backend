# **COVIDTrends Backend in Python, Postgres, Flask, & Docker**

## **What and why**

This is the backend part of a fullstack application. Ideally this application will serve as the database and API for COIVDTrends, a Canadian application dedicated to showing Canadians geographically relevant COVID-19 data.

## **Technology**

- Python along with Flask are used to communicate with the database and generate an API for the client to query the database.
- Postgres is used as the database. With Postgres our API can make SQL queries on the data.
- Docker will be used to containerize both the backend application, as well as the database. This will help with development and deployment on Windows Azure.

## **Steps to replicated**

1. (I haven't solidified anything, so this is TBA...)

## **Retrospective**

1. **Did you choose to use an ORM or raw SQL? Why?**
   I am aiming to use raw SQL within Flask. I hate the limited documentation of ORMs, along with the abstrction that ORMs produce. They prevent me from solidifying my understand of SQL. I would rather struggle with SQL and move slowly, than move quickly but be doomed to reading obscure forum posts on troubleshooting ORM issues.

2. **What future improvements are in store, if any?**

Meetings will be the hardest relationships to implement, because a meeting must belong to both one and only one companion and one and only one user.

## **API Endpoints Reference**

**Dev base_url: localhost:5000**

### **Endpoint Grouping One**

| METHOD | NAME               | PATH                                                     | RESULT                                           |
| ------ | ------------------ | -------------------------------------------------------- | ------------------------------------------------ |
| GET    | get all users      | base_url/users                                           | returns all recrods from the user_account table  |
| GET    | get single-user    | base_url/users/<span style="color:lightgreen">{id}<span> | returns single record based on id parameter      |
| POST   | create single user | base_url/users                                           | creates a new record based on valid JSON request |
| DELETE | delete single user | base_url/users/<span style="color:lightgreen">{id}<span> | deletes a record based on id parameter           |

Example of a valid post request:

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

## **Database Dump**

A database dump created by pg_dump can be found in `./data`

## **Insomnia API Endpoint Export**

tba../

## **Entity Relationship Diagrams**

tba...

# **Limitations & Shortcomings**

# **Successes**

- [✔️] utilized Flask's "blueprint" functionarlity to splitup my API routes into multiple files

# **Notes**
