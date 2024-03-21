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
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reserved_customer', null=True, default=None)
    table = models.ForeignKey(Table, on_delete=models.CASCADE, related_name='reserved_tables')
    date = models.DateField()
    time = models.TimeField()
    number_of_guests = models.IntegerField()

    class Meta:
        db_table = 'reservation'
    
    def __str__(self):
        return f"Reservation for {self.customer} at {self.date} {self.time}"

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
        return f"{self.request_text} for ({self.reservation}) (Approved: {self.is_approved})"
