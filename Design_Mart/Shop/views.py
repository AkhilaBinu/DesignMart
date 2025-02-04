from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import *
from .forms import *
from Guest.models import*
from django.contrib import messages
from Customer.models import *

# Create your views here.
def homepage(request):
    return render(request,"shophomepage.html")

def shop_homepage(request):
    if not request.session.get("sid"):
        return redirect("/Guest/Login/")
    customer_name = request.session.get("uname", "Customer")
    return render(request, "shophomepage.html", {"customer_name": customer_name})

def shop_design_list(request):
    designs = AddDesign.objects.all()  # Updated to use the correct model class
    return render(request, 'DisplayDesigns.html', {'designs': designs})







def add_dress(request):
    added_dress = None  # To hold the details of the added dress
    shop_id = request.session.get("sid")  # Get the logged-in shop's ID from the session

    # Ensure the shop is valid
    if not shop_id:
        return render(request, "error.html", {"message": "Shop not logged in."})  # Error page if shop is not logged in

    shop = Shop.objects.get(id=shop_id)  # Fetch the shop object using the session value

    if request.method == "POST":
        form = DressForm(request.POST, request.FILES)
        if form.is_valid():
            dress = form.save(commit=False)  # Create the dress object but don't save to the database yet
            dress.shop = shop  # Set the shop field
            dress.save()  # Now save the object to the database
            added_dress = dress  # Save the created dress object
    else:
        form = DressForm()

    # Get all dresses for the currently logged-in shop
    all_dresses = Dress.objects.filter(shop=shop)

    return render(
        request,
        "add_dress.html",
        {"form": form, "added_dress": added_dress, "all_dresses": all_dresses},
    )


# Edit dress
def edit_dress(request, dress_id):
    dress = get_object_or_404(Dress, id=dress_id)
    if request.method == "POST":
        form = DressForm(request.POST, request.FILES, instance=dress)
        if form.is_valid():
            form.save()
            return redirect('/Shop/add-dress/')
    else:
        form = DressForm(instance=dress)
    return render(request, 'edit_dress.html', {'form': form})

# Delete dress
def delete_dress(request, dress_id):
    dress = get_object_or_404(Dress, id=dress_id)
    dress.delete()
    return redirect('/Shop/add-dress/')

# views.py

def shop_orders(request):
    shop_id = request.session.get('sid')
    if not shop_id:
        messages.error(request, "You need to be logged in as a shop.")
        return redirect('/Shop/Login/')   
    shop = Shop.objects.get(id=shop_id)
    orders = Order.objects.filter(dress__shop=shop)
    return render(request, 'shop_orders.html', {'orders': orders, 'shop': shop})



def sdesign_booking_list(request):
    # Get the shop ID from the session
    shop_id = request.session.get("sid")
    
    if not shop_id:
        # If no shop is found in session, redirect to shop login
        return redirect('/Guest/Login/')

    # Retrieve the shop object using the shop ID
    try:
        shop = Shop.objects.get(id=shop_id)
    except Shop.DoesNotExist:
        # Handle the case where the shop does not exist
        return redirect('/Guest/Login/')

    # Fetch bookings where the shop matches the session's shop
    bookings = DesignBooking.objects.filter(shop=shop)

    # Return the bookings to the template
    return render(request, 'sview_booking.html', {'bookings': bookings})

    



def update_delivery_status(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    if request.method == 'POST':
        status = request.POST.get('status')
        if status:  # Check if the status value is not None
            order.status = status
            order.save()
            return redirect('/Shop/orders/')  # Redirect to the orders page

    return redirect('/Shop/order')  # In case of invalid status, just redirect


def shop_design_list(request):
    designs = AddDesign.objects.all()  # Get all designs added by customers
    return render(request, 'DisplayDesigns.html', {'designs': designs})



def book_design(request, design_id):
    try:
        # Get the design object
        design = AddDesign.objects.get(id=design_id)

        # Get the shop from the session
        shop_id = request.session.get('sid')  # Assuming shop_id is stored in session when shop logs in
        if not shop_id:
            return redirect('shop_login')  # If no shop is found in session, redirect to login

        # Get the shop object from the database
        shop = Shop.objects.get(id=shop_id)

        # Create the DesignBooking entry, using the customer from the design (design.user)
        DesignBooking.objects.create(
            design=design,
            shop=shop,
            # customer=design.user,  # Since customer is already in AddDesign, you don’t need this line
        )

        # Update the design status to 'booked'
        design.status = 'booked'
        design.save()

        # Redirect to the design list page
        return redirect('/Shop/shop_design_list')

    except AddDesign.DoesNotExist:
        return redirect('/Shop/shop_design_list')
