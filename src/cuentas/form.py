from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import Client, Adm, User
from django import forms

class clientRegister(UserCreationForm):
	first_name = forms.CharField(required=True)
	last_name = forms.CharField(required=True)

	class Meta(UserCreationForm.Meta): 
		model = User
		fields = [
			'first_name',
			'last_name',
			'email',
			'username',
		]
		labels = {
			'first_name' : 'nombre',
			'last_name' : 'apellido',
			'email' : 'email',
			'username' : 'usuario',
		}

	@transaction.atomic
	def save(self):
		user = super().save(commit=False)
		user.is_client = True
		user.save()
		client = Client.objects.create(user=user)
		client.first_name = self.cleaned_data.get('first_name')
		client.last_name = self.cleaned_data.get('last_name')
		return user
		
class adminRegister(UserCreationForm):
	first_name = forms.CharField(required=True)
	last_name = forms.CharField(required=True)

	class Meta(UserCreationForm.Meta):
		model = User

		fields = [
			'first_name',
			'last_name',
			'email',
			'username',
		]
		labels = {
			'first_name' : 'nombre',
			'last_name' : 'apellido',
			'email' : 'email',
			'username' : 'usuario',
		}

	@transaction.atomic 
	def save(self):
		user = super().save(commit=False)
		user.is_admin = True
		user.is_staff = True
		user.save()
		adm = Adm.objects.create(user=user)
		adm.first_name = self.cleaned_data.get('first_name')
		adm.last_name = self.cleaned_data.get('last_name')
		return user


        
class UpdateUser(forms.ModelForm):
    email = forms.EmailField(max_length=254, widget=forms.TextInput(attrs={'placeholder': 'Correo electronico'}))
    class Meta:
        model = User
        fields = ('username', 'email')

class AdmUpdate(forms.ModelForm):
    class Meta:
        model = Adm
        fields = ['photo']

class ClientUpdate(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['photo']