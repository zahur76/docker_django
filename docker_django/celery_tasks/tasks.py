from celery.schedules import crontab
from django.http import HttpResponse

from docker_django.celery import app as celery_app


@celery_app.task(bind=True)
def say_hello(self):
    print("hello")
    return HttpResponse(status=200)


# Triggered every 30 seconds
celery_app.add_periodic_task(
    crontab(),
    say_hello,
    name="say_hello",
)
