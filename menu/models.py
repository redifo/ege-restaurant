from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class MenuItem(models.Model):
    """model for a menu item"""
    
    #The choices list format learned from
    #https://docs.djangoproject.com/en/5.0/ref/models/fields/

    STARTER = 'Starter'
    MEZE = 'Meze'
    SALAD = 'Salad'
    MAIN_COURSE = 'Main Course'
    DESSERT = 'Dessert'
    BEVERAGE = 'Beverage'
    PIDE = 'Pide'
    STEAK = 'Steak'
    OTHER = 'Other'

    CATEGORY_CHOICES = [
        (STARTER, 'Starter'),
        (MEZE, 'Meze'),
        (SALAD, 'Salad'),
        (MAIN_COURSE, 'Main Course'),
        (DESSERT, 'Dessert'),
        (BEVERAGE, 'Beverage'),
        (PIDE, 'Pide'),
        (STEAK, 'Steak'),
        (OTHER, 'Other'),
    ]
    
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    is_available = models.BooleanField(default=True)
    image = CloudinaryField('image', default='placeholder')
    class Meta:
        db_table = 'menu'
        
    def __str__(self):
        return self.name