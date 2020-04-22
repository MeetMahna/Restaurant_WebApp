from django import forms
from .models import Item


class FoodForm(forms.ModelForm):
    class Meta:
        model = Item
        exclude = ['food','item_name', 'item_price']
    #item_qty = forms.ChoiceField(choices=((0,0), (1,1), (2,2), (3,3), (4,4), (5,5)))

