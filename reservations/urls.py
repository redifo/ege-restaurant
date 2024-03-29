from django.urls import path
from .views import make_reservation, reservation_success, edit_reservation, delete_reservation

urlpatterns = [
    path('', make_reservation, name="reservations"),
    path('success/<int:pk>', reservation_success, name="reservation_success"),
    path('reservation/edit/<int:pk>/', edit_reservation, name="edit_reservation"),
    path('reservation/delete/<int:pk>/', delete_reservation, name='delete_reservation'),
]
