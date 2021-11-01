from django import forms

class PriceForm(forms.Form):
    price_from = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-price_from form-price', 'id': 'form-price_from', 'value': 'form-price-from'}))
    price_to = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-price_to form-price', 'id': 'form-price_to', 'value': 'form-price-to'}))