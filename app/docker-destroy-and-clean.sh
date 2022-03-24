#!/bin/bash

docker compose down
sleep 2
docker compose down --rmi all --volumes