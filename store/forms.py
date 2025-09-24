from django import forms
from .models import *

class ProductForm(forms.ModelForm):
    class meta:
        model = Product
        fields = ['name', 'description', 'price', 'image']

class OrderItemForm(forms.ModelForm):
    class meta:
        model = OrderItem
        fields = ['product', 'quantity']