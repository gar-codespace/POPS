FILENAME = "login/views"
FILEDATE = 20240201


from django.shortcuts import render
from django.http import HttpResponse


def home_screen_first(request):
    return HttpResponse("Please log in")
