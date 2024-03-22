from django.urls import path
from .views import ReservedListView

urlpatterns = [
    path('', ReservedListView.as_view(), name="reservations")
    
]