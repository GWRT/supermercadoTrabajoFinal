from django import forms
from .models import Category

class categoryForm(forms.ModelForm):
	class Meta:
		model = Category
		fields = [
			'name',
			'desc',
		]
		labels = {
			'name' : 'Nombre',
			'desc' : 'Descripcion',
		}

	def __init__(self, *args, **kwargs):
		super(categoryForm,self).__init__(*args,**kwargs)
		self.fields['name'].widget.attrs.update({'class':'mdl-textfield__input'})
		self.fields['desc'].widget.attrs.update({'class':'mdl-textfield__input'})
		self.fields['name'].required = False
		self.fields['desc'].required = False	