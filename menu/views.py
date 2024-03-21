from django.shortcuts import render
from django.views.generic import ListView
from .models import MenuItem

class MenuListView(ListView):
    
    queryset = MenuItem.objects.filter(is_available=True) 
    template_name = "menu.html"  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = MenuItem.objects.filter(is_available=True) 
        categorized_items = {}
        for item in queryset:
            categorized_items.setdefault(item.get_category_display(), []).append(item)
        context['categorized_items'] = categorized_items
        return context