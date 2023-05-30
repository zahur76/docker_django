#!/bin/sh

# run a worker :)
celery -A docker_django worker --loglevel=info --concurrency 1 -E
