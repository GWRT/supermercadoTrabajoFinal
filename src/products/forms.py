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
		'disc',
		'cat',
		'prov',
		'stat',
		'img',
		]

	