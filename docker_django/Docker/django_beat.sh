#!/bin/sh

# run celery beat
celery -A docker_django beat
