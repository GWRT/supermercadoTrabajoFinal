from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = [
		'barcode',
		'name',
		'units',
		'price',
		'img',
		]

class Prod(forms.Form):
	barcode = forms.CharField(label='Barcode', max_length=20)
	name = forms.CharField(label='Name', max_length=20)
	units = forms.IntegerField(label='Units')
	price = forms.IntegerField(label='Price')
	img = forms.ImageField(label='Image')
	