from django import forms
from .models import Account
from django.contrib.auth.forms import User, PasswordChangeForm


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

    
    def __init__(self, *args, **kwargs):
        super(UpdateForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].help_text = None
            for field in self.fields:
                self.fields[field].widget.attrs = {
                    'class': 'form-control',
                }
        

class AccountUpdate(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['photo']


class PasswordChangeForm(PasswordChangeForm):
   
    def __init__(self, *args, **kwargs):
        super(PasswordChangeForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {
                'class' : 'form-control'
            }
        self.fields['old_password'].label = 'Introduzca su antigua contraseña'
        self.fields['new_password1'].label = 'Introduzca su nueva contraseña'
        self.fields['new_password2'].label = 'Repita su nueva contraseña'


    

