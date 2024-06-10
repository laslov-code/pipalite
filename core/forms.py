from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].widget.attrs.update({
            'required':'',
            'class':'form-control',
            'maxlength':'20',
            'minlength':'6',
            'name':'username',
            'id':'username',
            'placeholder':'Enter your Username',
            'autofocus':'',
        })
        self.fields['email'].widget.attrs.update({
            'required':'',
            'class':'form-control',
            'maxlength':'50',
            'minlength':'6',
            'name':'email',
            'id':'email',
            'placeholder':'Enter your email',
        })
        self.fields['password1'].widget.attrs.update({
            'required':'',
            'class':'form-control',
            'maxlength':'20',
            'minlength':'6',
            'name':'password1',
            'id':'password1',
            'placeholder':'Enter your password',
        })
        self.fields['password2'].widget.attrs.update({
            'required':'',
            'class':'form-control',
            'maxlength':'20',
            'minlength':'6',
            'name':'password2',
            'id':'password2',
            'placeholder':'Confirm your password',
        })
    class Meta: 
        model = User
        fields = ['username', 'email','password1', 'password2']

