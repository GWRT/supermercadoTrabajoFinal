from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User
from accounts.models import Account
	
class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30, widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {
                'class': 'mdl-textfield__input',
            }
        self.fields['username'].label = "USUARIO"    
        self.fields['password'].label = "CONTRASEÑA" 
    
    class Meta:
        model = User
        fields = ['username', 'password']
        

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

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {
                'class': 'mdl-textfield__input',
            }
