from django import forms
from .models import *




class ShopRegistrationForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ['shop_name', 'owner_name', 'contact_number', 'email', 'address', 'password', 'proof', 'Logo', 'district', 'place']
        widgets = {
            'shop_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Shop Name'}),
            'owner_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Owner Name'}),
            'contact_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Contact Number'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Address', 'rows': 3}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Password'}),
            'proof': forms.FileInput(attrs={'class': 'form-control'}),
            'Logo': forms.FileInput(attrs={'class': 'form-control'}),
            'district': forms.Select(attrs={'class': 'form-control'}),
            'place': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Place'}),
        }


 


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['full_name', 'phone_number', 'address', 'email', 'district', 'place', 'password', 'photo']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Full Name'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Phone Number'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Address', 'rows': 3}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'}),
            'district': forms.Select(attrs={'class': 'form-control'}),
            'place': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Place'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Password'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
        }

      