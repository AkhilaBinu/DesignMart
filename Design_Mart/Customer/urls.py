from django.urls import path
from .import views

urlpatterns = [
path('adddesign/', views.add_design, name='add_design'),
path('list/', views.design_list, name='design_list'),
path("homepage/", views.customer_homepage, name="customer_homepage"),
path('delete-design/<int:design_id>/', views.delete_design, name='delete_design'),
path('dresses/', views.customer_view_dresses, name='customer_view_dresses'),
path('dress/<int:pk>/', views.dress_detail, name='dress_detail'),
path('buy-now/<int:pk>/', views.buy_now, name='buy_now'),
path('confirm/<int:pk>/', views.confirm_order, name='confirm_order'),
    path('order/', views.order_detail, name='order_detail'),
    path('customer_profile/', views.customer_profile, name='customer_profile'),
    path('design-booking-list/', views.design_booking_list, name='design_booking_list'),
]