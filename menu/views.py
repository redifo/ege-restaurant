from django.shortcuts import render
from django.views.generic import ListView
from .models import MenuItem

class MenuListView(ListView):
    
    queryset = MenuItem.objects.filter(is_available=True) 
    template_name = "menu.html"  