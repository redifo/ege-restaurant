from django.contrib import admin
from .models import SpecialRequest, Reservation, Table

@admin.register(SpecialRequest)
class SpecialRequestAdmin(admin.ModelAdmin):
    list_display = ['request_text', 'is_approved']
    list_filter = ['is_approved']
    search_fields = ['request_text']

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ['customer', 'date', 'time', 'number_of_guests']
    list_filter = ['date', 'time']
    search_fields = ['customer__name', 'table__table_number']

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ['table_number', 'capacity', 'table_location']
    list_filter = ['table_location']
    search_fields = ['table_number', 'table_location']
