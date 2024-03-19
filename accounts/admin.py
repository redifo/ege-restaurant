from django.contrib import admin
from .models import Customer

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'created_at')
    list_filter = ('created_at', 'email')  

admin.site.register(Customer, CustomerAdmin)
