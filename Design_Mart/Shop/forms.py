from django import forms
from .models import Dress


class DressForm(forms.ModelForm):
    class Meta:
        model = Dress
        fields = [
            'name', 'description', 'price', 'stock', 'category',
            'size', 'color', 'material', 'image'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Dress Name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Enter Description'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Price'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Stock Quantity'}),
            'category': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Category'}),
            'size': forms.Select(attrs={'class': 'form-select'}),
            'color': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Color'}),
            'material': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Material'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }

