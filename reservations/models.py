from django.db import models
from django.contrib.auth.models import User

class Table(models.Model):
    """
    model for a table in the restaurant
    """
    GARDEN = 'Garden'
    BAR = 'Bar'
    LOCATION_CHOICES = [
        (GARDEN, 'Garden'),
        (BAR, 'Bar')
    ]

    table_number = models.IntegerField(unique=True)
    capacity = models.IntegerField()
    table_location = models.CharField(max_length=50, choices=LOCATION_CHOICES)

    class Meta:
        db_table = 'table'
        
    def __str__(self):
        return f"Table {self.table_number} at {self.table_location}"

class Reservation(models.Model):
    """
    model for each reservation
    """
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reserved_customer', blank=True, null=True)
    email  = models.EmailField(blank=True, null=True)
    phone =  models.CharField(max_length=15, blank=True, null=True)
    name  = models.CharField(max_length=50, blank=True, null=True)
    table = models.ForeignKey(Table, on_delete=models.CASCADE, related_name='reserved_tables')
    date = models.DateField()
    time = models.TimeField()
    number_of_guests = models.IntegerField()
    created_at =  models.DateTimeField(auto_now_add=True)
    updated_at =  models.DateTimeField(auto_now=True)
    status= models.BooleanField(default=False) # True if confirmed else False
    class Meta:
        db_table = 'reservation'
    
    def __str__(self):
        if self.customer:
            return f"Reservation for {self.customer.username} at {self.date} {self.time}"
        else:
            return f"Reservation for {self.name} at {self.date} {self.time}"

class SpecialRequest(models.Model):
    """
    model for a special request made on a reservation
    """
    content = models.TextField()
    is_approved = models.BooleanField(default=False)
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE, related_name='reservation_special_requests')

    class Meta:
        db_table = 'special_request'

    def __str__(self):
        return f"{self.content} for ({self.reservation}) (Approved: {self.is_approved})"
