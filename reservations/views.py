from django.shortcuts import render
from django.views.generic import ListView
from .models import Reservation

class ReservedTable(ListView):
    
    queryset = Reservation.objects.filter(name="kaan") 
    template_name = "reservations.html"  
