from django.shortcuts import render
from django.http import HttpResponse
from .models  import Reservation


def reserve_table(request):
    if request.method == 'POST': 
        pass

def my_reservations(request):
    return HttpResponse("This is the reservations page.")