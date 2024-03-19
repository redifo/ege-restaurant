from django.contrib import admin
from .models import MenuItem

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'category')  
    search_fields = ('name', 'description', 'category')  
    list_filter = ('category',) 

admin.site.register(MenuItem, MenuItemAdmin)
