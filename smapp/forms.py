from dataclasses import fields
from django import forms
from .models import *

class ProductFrom(forms.ModelForm):
    class Meta:
        model=product
        fields=[
            'prod_name',
            'prod_sku',
            'prod_price',
            'prod_quantity',
            'prod_image'
        ]
