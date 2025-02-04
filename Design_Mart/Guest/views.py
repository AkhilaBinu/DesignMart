from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib import messages


# Create your views here.

def home(request):
    return render(request,"Homepage.html")




from django.contrib.auth import authenticate, login





def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Try logging in as a Shop first
        shop = Shop.objects.filter(email=username).first()
        if shop and shop.password == password:  # Replace with check_password() for hashed passwords
            request.session["sid"] = shop.id
            request.session["uname"] = shop.shop_name
            messages.success(request, "Shop login successful!")
            return redirect("/Shop/shomepage/")
        
        # If no Shop matches, try logging in as a Customer
        customer = Customer.objects.filter(email=username).first()
        if customer and customer.password == password:  # Replace with check_password() for hashed passwords
            request.session["cid"] = customer.id
            request.session["cname"] = customer.full_name
            messages.success(request, "Customer login successful!")
            return redirect("/Customer/homepage/",)

        # If neither matches, return an error
        messages.error(request, "Invalid email or password. Please try again.")
        return redirect("/Guest/Login/")

    return render(request, "Login.html")






def register_shop(request):
    if request.method == 'POST':
        form = ShopRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('/Guest/Login/')  
    else:
        form = ShopRegistrationForm()
    return render(request, 'Shop.html', {'form': form})



def register_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save() 
        return redirect('/Guest/Login/')  
    else:
        form = CustomerForm()
    
    return render(request, 'Customer_registration.html', {'form': form})

   