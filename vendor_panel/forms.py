# forms.py
from django import forms
from .models import Shop, VendorService

class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ['name', 'city', 'state', 'country', 'address', 'pincode', 'image', 'user']

class VendorServiceForm(forms.ModelForm):
    class Meta:
        model = VendorService
        fields = ['service', 'paid', 'shop']
