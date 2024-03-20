from django.views.generic import ListView
from .models import MenuItem

class MenuListView(ListView):
    model = MenuItem
    queryset = MenuItem.objects.filter(is_available=True) 
    template_name = "menu.html"  