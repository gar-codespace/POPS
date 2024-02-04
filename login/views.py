FILENAME = "login/views"
FILEDATE = 20240201


from django.shortcuts import render

# from django.http import HttpResponse

from django.views.generic import TemplateView


# def home_screen_first(request):
#     return HttpResponse("Log in please")


class HomeScreenFirst(TemplateView):
    template_name = "home.html"


class AboutPage(TemplateView):
    template_name = "about.html"


class HelpPage(TemplateView):
    template_name = "help.html"
