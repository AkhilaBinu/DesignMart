from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Shop, Customer

@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'shop_name', 'owner_name', 'contact_number', 'email', 
        'place', 'district', 'date_joined'
    )  # Display these fields in the list view
    list_filter = ('district', 'date_joined')  # Add filters for district and date_joined
    search_fields = ('shop_name', 'owner_name', 'email', 'place', 'district')  # Enable search
    readonly_fields = ('date_joined',)  # Make date_joined read-only
    ordering = ('-date_joined',)  # Order by date_joined in descending order

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'full_name', 'phone_number', 'email', 'place', 
        'district', 'date_joined'
    )  # Display these fields in the list view
    list_filter = ('district', 'date_joined')  # Add filters for district and date_joined
    search_fields = ('full_name', 'email', 'phone_number', 'place', 'district')  # Enable search
    readonly_fields = ('date_joined',)  # Make date_joined read-only
    ordering = ('-date_joined',)  # Order by date_joined in descending order
