from django.contrib import admin
from .models import Email, ReservationEmail

@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    list_display = ('subject', 'recipient', 'sent_at')
    list_filter = ('sent_at',)
    search_fields = ('subject', 'recipient')

@admin.register(ReservationEmail)
class ReservationEmailAdmin(admin.ModelAdmin):
    list_display = ('reservation', 'email')
    list_filter = ('reservation__date',)  
    search_fields = ('reservation__customer__name', 'email__subject')  
