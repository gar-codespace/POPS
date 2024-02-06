FILENAME = "login/urls"
FILEDATE = 20240201

from django.urls import path

from .views import HomeScreenFirst, AboutPage, HelpPage

urlpatterns = [
    path("", HomeScreenFirst.as_view(), name="home"),
    path("about/", AboutPage.as_view(), name="about"),
    path("help/", HelpPage.as_view(), name="help"),
]
