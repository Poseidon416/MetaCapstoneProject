from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Menu(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    num_guests = models.IntegerField(
        validators=[MaxValueValidator(6), MinValueValidator(0)]
    )
    booking_date = models.DateTimeField()
    
class Booking(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField(
        validators=[MaxValueValidator(5), MinValueValidator(0)]
    )