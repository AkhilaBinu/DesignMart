from django.db import models

dis=[('ernakulam','Ernakulam'),('kollam','Kollam'),('idukki','Idukki')]

# Create your models here.
class Shop(models.Model):
    shop_name = models.CharField(max_length=100)
    owner_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    place=models.CharField(max_length=100)
    district = models.CharField(max_length=20, choices=dis)
    date_joined = models.DateTimeField(auto_now_add=True)
    password = models.CharField(max_length=100)
    proof=models.ImageField(upload_to="Shop_proof/")
    Logo=models.ImageField(upload_to="Shop_logo/")



class Customer(models.Model):
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    place=models.CharField(max_length=100)
    district = models.CharField(max_length=20, choices=dis)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    photo=models.ImageField(upload_to="Customer_image/")
    date_joined = models.DateTimeField(auto_now_add=True)


