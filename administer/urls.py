# administer/urls.py

FILENAME = "administer/urls"
FILEREV = 20240201

from django.urls import path

from .views import home_page_view

urlpatterns = [
    path("", home_page_view, name="home"),
]
