from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def my_accounts(request):
    return HttpResponse("This is the accounts page.")