from dataclasses import field
from django import forms
from .models import Producto

class ProductForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'