from django.contrib import admin
from .models import AddDesign, Order, DesignBooking

@admin.register(AddDesign)
class AddDesignAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user', 'price', 'status', 'date_added')  # Display these fields in the admin list view
    list_filter = ('status', 'date_added')  # Add filters for status and date
    search_fields = ('name', 'user__name', 'status')  # Enable search by name, user, and status
    list_editable = ('status',)  # Allow inline editing of status
    readonly_fields = ('date_added',)  # Make date_added read-only


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'dress', 'quantity', 'total_price', 'status', 'created_at', 'updated_at')  # Display key fields
    list_filter = ('status', 'created_at')  # Add filters for status and creation date
    search_fields = ('user__name', 'dress__name', 'status')  # Enable search by user, dress name, and status
    list_editable = ('status',)  # Allow inline editing of status
    readonly_fields = ('created_at', 'updated_at')  # Make timestamps read-only


@admin.register(DesignBooking)
class DesignBookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'design', 'shop', 'booking_date')  # Display these fields
    list_filter = ('booking_date',)  # Add a filter for the booking date
    search_fields = ('design__name', 'shop__name')  # Enable search by design and shop names
    readonly_fields = ('booking_date',)  # Make booking_date read-only
