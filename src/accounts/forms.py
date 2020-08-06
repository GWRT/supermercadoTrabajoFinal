from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User
	
class SignUpForm(UserCreationForm):
	first_name = forms.CharField(max_length=30, required=False)
	last_name = forms.CharField(max_length=30, required=False)
	email = forms.EmailField(max_length=254, help_text='Required')

	class Meta:
		model = User
		fields = (
			'username',
			'first_name',
			'last_name',
			'email',
			'password1',
			'password2',
		)
		labels = {
			'first_name' : 'Nombre',
			'username' : 'Usuario',
			'last_name' : 'Apellido',
			'email' : 'Correo',
			'password1' : 'Contraseña',
			'password2' : 'Repita_Contraseña',
		}

	def __init__(self, *args, **kwargs):
		super(SignUpForm,self).__init__(*args,**kwargs)
		self.fields['username'].widget.attrs.update({'class':'mdl-textfield__input'})
		self.fields['first_name'].widget.attrs.update({'class':'mdl-textfield__input'})
		self.fields['last_name'].widget.attrs.update({'class':'mdl-textfield__input'})
		self.fields['email'].widget.attrs.update({'class':'mdl-textfield__input'})
		self.fields['password1'].widget.attrs.update({'class':'mdl-textfield__input'})
		self.fields['password2'].widget.attrs.update({'class':'mdl-textfield__input'})
