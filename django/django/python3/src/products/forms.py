from pyexpat import model
from django import forms

from .models import Purchase
class PurchaseForm(forms.ModelForm):
    class Meta:
        model=Purchase
        fields=['product','price','quantity']
