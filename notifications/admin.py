from django.contrib import admin
from .models import Email
from django_summernote.admin import SummernoteModelAdmin
@admin.register(Email)
class EmailAdmin(SummernoteModelAdmin):
    list_display = ('subject', 'recipient', 'sent_at')
    list_filter = ('sent_at',)
    search_fields = ('subject', 'recipient')

