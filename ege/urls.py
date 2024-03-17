"""
URL configuration for ege project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from accounts.views import my_accounts
from menu.views import my_menu
from reservations.views import my_reservations

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", my_accounts, name='accounts'), #  Default view when accessing root of site CHANGEEEEEE LATERRR
    path('accounts/', my_accounts, name='accounts'),  # Add accounts URLs
    path('menu/', my_menu, name='menu'),              # Add menu URLs
    path('reservations/', my_reservations, name='reservations'),  # Add reservations URLs
]
