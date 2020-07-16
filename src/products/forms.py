from django import forms
from .models import Product
from categoria.models import Category
from provider.models import Provider

class ProductForm(forms.ModelForm):
	barcode = forms.IntegerField()
	name = forms.CharField()
	units = forms.IntegerField()
	price = forms.IntegerField()
	disc = forms.IntegerField()
	cat = forms.ModelChoiceField(queryset = Category.objects.all(), initial = 0)
	prov = forms.ModelChoiceField(queryset = Provider.objects.all(), initial = 0)
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

	