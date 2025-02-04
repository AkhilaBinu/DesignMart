from django.db import models
from Customer.models import *
from Guest.models import *
# Create your models here.
class Dress(models.Model):
    name = models.CharField(max_length=200)  # Name of the dress
    description = models.TextField(blank=True)  # Optional description
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price with two decimal places
    stock = models.PositiveIntegerField()  # Quantity available
    category = models.CharField(max_length=200)  # Dress category
    size_choices = [
        ('XS', 'Extra Small'),
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
    ]
    size = models.CharField(max_length=2, choices=size_choices)  # Size of the dress
    color = models.CharField(max_length=50)  # Dress color
    material = models.CharField(max_length=100, blank=True)  # Material of the dress
    image = models.ImageField(upload_to='dresses/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    shop=models.ForeignKey(Shop, on_delete=models.CASCADE)



    