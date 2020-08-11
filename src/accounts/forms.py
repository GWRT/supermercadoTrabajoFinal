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

    
    def __init__(self, *args, **kwargs):
        super(UpdateForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {
                'class': 'form-control',
            }
            self.fields[field].help_text = None
        

class AccountUpdate(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['photo']

    
    def __init__(self, *args, **kwargs):
        super(AccountUpdate, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {
                'class': 'form-control',
            }
