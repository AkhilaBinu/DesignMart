from django.urls import path
from .import views

urlpatterns = [
path("shomepage/", views.shop_homepage, name="shop_homepage"),
path('shop_design_list/', views.shop_design_list, name='shop_design_list'),
path("add-dress/", views.add_dress, name="add_dress"),
path('edit/<int:dress_id>/', views.edit_dress, name='edit_dress'),
path('delete/<int:dress_id>/', views.delete_dress, name='delete_dress'),

path('orders/', views.shop_orders, name='shop_orders'),
    path('update-delivery-status/<int:order_id>/', views.update_delivery_status, name='update_delivery_status'),
    path('book-design/<int:design_id>/', views.book_design, name='book_design'),
    path('sdesign_booking_list/', views.sdesign_booking_list, name='sdesign_booking_list'),
]