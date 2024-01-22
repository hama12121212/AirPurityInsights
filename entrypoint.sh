#!/bin/bash

# Wait for PostgreSQL to start
# Host and port can be changed based on your setup
echo "Waiting for PostgreSQL to start..."
while ! nc -z db 5432; do
  echo -n "."
  sleep 1
done
echo -e "\nPostgreSQL started"

# Run the command
echo "Starting Flask application"
exec flask --app src run --host=0.0.0.0 -p 8888
