from django import forms
from .models import Product
from categoria.models import Category
from provider.models import Provider

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

	