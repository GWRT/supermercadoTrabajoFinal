from django import forms
from .models import Account

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['user', 'photo']
        widgets = {
            'user': forms.TextInput(attrs={'class': 'form-control'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
        } 

