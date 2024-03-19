from django.db import models

# Create your models here.

class Customer(models.Model):
    """
    Model representing a customer.
    """
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
