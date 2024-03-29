from django.shortcuts import render
from .models import MenuItem


def MenuListView(request):
    categories = MenuItem.objects.order_by().values_list(
        'category', flat=True).distinct()
    menu_items = MenuItem.objects.all()
    context = {
        'categories': categories,
        'menu_items': menu_items,
    }
    return render(request, 'menu.html', context)
