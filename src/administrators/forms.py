from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User
	
class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Usuario'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Costraseña'}))

    class Meta:
        model = User
        fields = ('username', 'password')

class SignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Usuario'}))
    first_name = forms.CharField(max_length=30,  widget=forms.TextInput(attrs={'placeholder': 'Nombre'}))
    last_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Apellido'}))
    email = forms.EmailField(max_length=254, widget=forms.TextInput(attrs={'placeholder': 'Correo electronico'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Costraseña'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirmar contraseña'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name','email', 'password1', 'password2')
 