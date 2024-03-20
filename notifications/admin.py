from django.contrib import admin
from .models import Email

@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    list_display = ('subject', 'recipient', 'sent_at')
    list_filter = ('sent_at',)
    search_fields = ('subject', 'recipient')

