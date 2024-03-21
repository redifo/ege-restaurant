from django.urls import path
from .views import my_reservations

urlpatterns = [
    path('', my_reservations.as_view(), name="my_reservations")
    
]