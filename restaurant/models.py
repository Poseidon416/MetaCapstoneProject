from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Booking(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    num_guests = models.IntegerField(default=1,
        validators=[MaxValueValidator(6), MinValueValidator(0)]
    )
    booking_date = models.DateTimeField(auto_now=True)
    
    
    
class Menu(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField(default=10,
        validators=[MaxValueValidator(5), MinValueValidator(0)]
    )
    
    def __str__(self):
        return f'{self.title} : {str(self.price)}'
    