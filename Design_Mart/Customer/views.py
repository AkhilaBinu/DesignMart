from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import *
from .forms import *
from Guest.models import Customer
# Create your views here.
from django.contrib import messages
from Shop.models import *
from django.contrib.auth.decorators import login_required


# def customer_profile(request):
#     if "role" not in request.session or request.session["role"] != "customer":
#         messages.error(request, "Unauthorized access. Please log in as a customer.")
#         return redirect("/Guest/Login/")  # Redirect to login page

#     customer = get_object_or_404(Customer, id=request.session["cid"])
#     return render(request, "customer_profile.html", {"customer": customer})

def customer_profile(request):
    customer_id = request.session.get("cid")
    if customer_id:
        customer = Customer.objects.get(id=customer_id)
        return render(request, "customer_profile.html", {"customer": customer})
    else:
        return redirect("/Customer/Login/")

def add_design(request):
    if request.method == 'POST':
        form = DesignForm(request.POST, request.FILES)
        if form.is_valid():
            design = form.save(commit=False)  
            customer_id = request.session["cid"] 
            if customer_id:
                try:
                    design.user = Customer.objects.get(id=customer_id) 
                    design.save() 
                    return redirect('/Customer/adddesign/')
                except Shop.DoesNotExist:
                    messages.error(request, "Invalid shop session. Please log in again.")
                    return redirect('/Guest/Login/')
            else:
                messages.error(request, "No shop logged in. Please log in first.")
                return redirect('/Guest/Login/')
    else:
        form = DesignForm()
    customer_id = request.session["cid"] 
    

    return render(request, 'Adddesign.html', {'form': form,})






def design_list(request):
    try:
        username = request.session.get('cid')  
        if not username:
            return HttpResponse("User is not logged in.", status=403)

        designs = AddDesign.objects.all()  # Updated to use the correct model class
        return render(request, 'listdesign.html', {'designs': designs})
    except Exception as e:
        return HttpResponse(f"Error: {str(e)}", status=500)

def customer_homepage(request):
    if not request.session.get("cid"):
        return redirect("/Guest/Login/")
    customer_name = request.session.get("uname", "Customer")
    return render(request, "customerhomepage.html", {"customer_name": customer_name})


def delete_design(request, design_id):
    deldesign = get_object_or_404(AddDesign, id=design_id)
    if request.method == 'POST':
        deldesign.delete()
        return redirect('/Customer/list/')
    return render(request, 'deletepet.html', {'pet': deldesign})



def customer_view_dresses(request):
    dresses = Dress.objects.all()  # Fetch all dresses
    return render(request, "Viewproduct.html", {"dresses": dresses})

def dress_detail(request, pk):
    # Get the dress object or return 404 if not found
    dress = get_object_or_404(Dress, pk=pk)
    return render(request, "dress_detail.html", {"dress": dress})









# Confirm Order View
def confirm_order(request, pk):
    # Get the dress object
    dress = get_object_or_404(Dress, pk=pk)

    # Ensure the customer is logged in
    customer_id = request.session.get("cid")
    if not customer_id:
        messages.error(request, "You need to be logged in to proceed.")
        return redirect('/Guest/Login/')

    # Render the confirmation page with dress details
    return render(request, 'confirm_order.html', {'dress': dress})
# Finalize the Order

def buy_now(request, pk):
    # Get the dress object
    dress = get_object_or_404(Dress, pk=pk)

    # Ensure the customer is logged in
    customer_id = request.session.get("cid")
    if not customer_id:
        messages.error(request, "You need to be logged in to make a purchase.")
        return redirect('/Guest/Login/')

    # Get the customer object
    try:
        customer = Customer.objects.get(id=customer_id)
    except Customer.DoesNotExist:
        messages.error(request, "Customer not found. Please log in again.")
        return redirect('/Guest/Login/')

    # Check if the dress is in stock
    if dress.stock <= 0:
        messages.error(request, f"Sorry, {dress.name} is out of stock.")
        return redirect('/Customer/homepage/')

    # Check if the user confirmed the order
    if request.method == "POST":
        # Create the order
        try:
            order = Order.objects.create(
                user=customer,
                dress=dress,
                quantity=1,
                total_price=dress.price
            )

            # Reduce stock
            dress.stock -= 1
            dress.save()

            messages.success(request, f"Successfully placed an order for {dress.name}!")
            return redirect('order_details', pk=order.pk)

        except Exception as e:
            messages.error(request, "There was an issue placing your order. Please try again.")
            return redirect('/Customer/homepage/')
    else:
        messages.error(request, "Order not confirmed.")
        return redirect('confirm_order', pk=pk)





def order_detail(request):
    customer_id = request.session.get("cid")
    
    if not customer_id:
        messages.error(request, "You need to be logged in to view your orders.")
        return redirect('/Guest/Login/')
    customer = get_object_or_404(Customer, id=customer_id)
    
    # Get all orders related to the logged-in customer
    orders = Order.objects.filter(user=customer)
    
    return render(request, 'order_detail.html', {'orders': orders})



def design_booking_list(request):
    customer_id = request.session.get("cid")
    customer = Customer.objects.get(id=customer_id)
    bookings = DesignBooking.objects.filter(design__user=customer)
    return render(request, 'viewbooking.html', {'bookings': bookings})



