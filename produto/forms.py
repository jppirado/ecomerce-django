from dataclasses import fields
from django import forms
from carrosapp.models import Supplier
from .models import Product  

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name_product', 'quantity_product' , 'fornecedor')

