from django.urls import path
from .import views

urlpatterns = [
  path('Homepage/',views.home),
  path("Login/", views.login, name="Login"),

  path('ShopRegister/',views.register_shop,name="register_shop"),
  path('Register/',views.register_customer,name="register_customer"),


  
  

    

]