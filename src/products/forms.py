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
		labels = {
			'barcode' : 'Barcode',
			'name' : 'Name',
			'units' : 'Units',
			'price' : 'Price',
			'disc' : 'Diccount',
			'cat' : 'Category',
			'prov' : 'Provider',
			'stat' : 'Status',
			'img' : 'Image',
		}

	def __init__(self, *args, **kwargs):
		super(ProductForm,self).__init__(*args,**kwargs)
		self.fields['barcode'].widget.attrs.update({'class':'mdl-textfield__input'})
		self.fields['name'].widget.attrs.update({'class':'mdl-textfield__input'})
		self.fields['units'].widget.attrs.update({'class':'mdl-textfield__input'})
		self.fields['price'].widget.attrs.update({'class':'mdl-textfield__input'})
		self.fields['disc'].widget.attrs.update({'class':'mdl-textfield__input'})
		self.fields['cat'].widget.attrs.update({'class':'mdl-cell mdl-cell--12-col'})
		self.fields['prov'].widget.attrs.update({'class':'mdl-cell mdl-cell--12-col'})
		self.fields['stat'].widget.attrs.update({'class':'mdl-cell mdl-cell--12-col'})

		self.fields['prov'].queryset = Provider.objects.exclude(estado = '2')

	