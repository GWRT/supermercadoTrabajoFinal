from django import forms
from .models import Account
from django.contrib.auth.forms import User


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['user', 'photo']
        widgets = {
            'user': forms.TextInput(attrs={'class': 'form-control'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
        }
        
class UpdateForm(forms.ModelForm):
    email = forms.EmailField(max_length=254, widget=forms.TextInput(attrs={'placeholder': 'Correo electronico'}))
    class Meta:
        model = User
        fields = ('username', 'email')


<<<<<<< HEAD
<<<<<<< HEAD
=======
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
>>>>>>> 459d354b9c2272a5fc640cded2edff0c46bcfa03
=======
class AccountUpdate(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['photo']
>>>>>>> rama2
