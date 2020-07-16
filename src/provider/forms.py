from django import forms
from .models import Provider

class providerForm(forms.ModelForm):
	class Meta:
		model = Provider
		fields = [
			'ruc',
			'razonSocial',
			'persona',
			'direccion',
			'email',
			'telefono',
			'estado',
		]
		labels = {
			'ruc' : 'RUC',
			'razonSocial' : 'Razon Social',
			'persona' : 'Persona de Contacto',
			'direccion' : 'Direccion',
			'email' : 'email',
			'telefono' : 'celular',
			'estado' : 'Estado'
		}

	def __init__(self, *args, **kwargs):
		super(providerForm,self).__init__(*args,**kwargs)
		self.fields['ruc'].widget.attrs.update({'class':'mdl-textfield__input'})
		self.fields['razonSocial'].widget.attrs.update({'class':'mdl-textfield__input'})
		self.fields['persona'].widget.attrs.update({'class':'mdl-textfield__input'})
		self.fields['direccion'].widget.attrs.update({'class':'mdl-textfield__input'})	
		self.fields['email'].widget.attrs.update({'class':'mdl-textfield__input'})	
		self.fields['telefono'].widget.attrs.update({'class':'mdl-textfield__input'})
		self.fields['estado'].widget.attrs.update({'class':'mdl-checkbox__input'})					
