from celery import shared_task
from django.http import HttpResponse

from docker_django.celery import app


@shared_task
def say_hello():
    print("hello")
    return HttpResponse(status=200)
