from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class Home(TemplateView):
    """
    Show the home page.
    """
    template_name = "home.html"


class Login(TemplateView):
    """
    Show the login/register page.
    """
    template_name = "login.html"