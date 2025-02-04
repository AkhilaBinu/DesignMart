from django.contrib import admin
from .models import Dress

@admin.register(Dress)
class DressAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'price', 'stock', 'category', 'size', 'color', 'material', 'shop', 'created_at'
    )  # Display these fields in the list view
    list_filter = ('category', 'size', 'color', 'shop', 'created_at')  # Add filters for category, size, color, and shop
    search_fields = ('name', 'description', 'category', 'color', 'shop__name')  # Enable search for specific fields
    list_editable = ('price', 'stock', 'size')  # Allow inline editing for price, stock, and size
    readonly_fields = ('created_at',)  # Make the created_at field read-only
    ordering = ('-created_at',)  # Order by the most recently created items by default
