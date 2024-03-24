from django.urls import path
from .views import MenuListView

urlpatterns = [
    path('', MenuListView, name="menu")
    
]