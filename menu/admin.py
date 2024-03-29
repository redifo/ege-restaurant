from django.contrib import admin
from .models import MenuItem
from django_summernote.admin import SummernoteModelAdmin


class MenuItemAdmin(SummernoteModelAdmin):
    list_display = ('name', 'description', 'price', 'category')
    search_fields = ('name', 'description', 'category')
    list_filter = ('category',)
    summernote_fields = ('description',)


admin.site.register(MenuItem, MenuItemAdmin)
