from celery_tasks import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="home"),
]
