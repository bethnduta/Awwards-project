from django.db import DJANGO_VERSION_PICKLE_KEY

from django.urls import URLPattern, path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
]