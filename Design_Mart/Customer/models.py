from django.db import models
from Guest.models import*
from Shop.models import Dress

# Create your models here.
class AddDesign(models.Model):  # Changed the class name to avoid conflicts
    name = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)
    discription = models.TextField(blank=True, null=True)
    price = models.CharField(max_length=50)
    design_pic = models.ImageField(upload_to="design/")
    user=models.ForeignKey(Customer, on_delete=models.CASCADE)
    status=models.CharField(default="pending",max_length=10)

    def __str__(self):
        return self.name
    

class Order(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)  # Customer placing the order
    dress = models.ForeignKey(Dress, on_delete=models.CASCADE)  # The dress being ordered
    quantity = models.PositiveIntegerField(default=1)  # Quantity of dresses ordered
    total_price = models.DecimalField(max_digits=10, decimal_places=2)  # Total price for the order
    status = models.CharField(max_length=10, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)  

    def __str__(self):
        return f"Order {self.id} - {self.dress.name}"
    

class DesignBooking(models.Model):
    design = models.ForeignKey(AddDesign, on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)