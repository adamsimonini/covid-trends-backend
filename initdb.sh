#!/bin/sh -e

psql --variable=ON_ERROR_STOP=1 --username "postgres" <<-EOSQL
    CREATE DATABASE "public_health_trends" OWNER = postgres;
    GRANT ALL PRIVILEGES ON DATABASE "public_health_trends" TO postgres;
EOSQL