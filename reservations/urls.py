from django.urls import path
from .views import make_reservation, reservation_success, edit_reservation

urlpatterns = [
    path('', make_reservation, name="reservations"),
    path('success/<int:pk>', reservation_success, name="reservation_success"),
    path('edit/', edit_reservation, name="edit_reservation")
]