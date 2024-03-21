from django.urls import path
from .views import ReservedTable

urlpatterns = [
    path('', ReservedTable.as_view(), name="ReservedTable")
    
]