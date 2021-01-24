from django import forms

from .models import MenuModel


class MenuForm(forms.ModelForm):
    class Meta:
        model = MenuModel
        fields = (
            'food_name',
            'food_pic',
            'food_cat',
            'food_price',
        )
