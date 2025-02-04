from django import forms
from .models import *


class DesignForm(forms.ModelForm):
    class Meta:
        model = AddDesign
        fields = ['name', 'discription', 'price', 'design_pic']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Design Name'}),
            'discription': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Description', 'rows': 3}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Price'}),
            'design_pic': forms.FileInput(attrs={'class': 'form-control'}),
        }

      