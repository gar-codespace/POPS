FILENAME = "login/urls"
FILEDATE = 20240201

from django.urls import path

from .views import home_screen_first

urlpatterns = [
    path("", home_screen_first, name="home"),
]
