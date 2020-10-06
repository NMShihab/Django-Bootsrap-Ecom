from django import forms
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User
from Login_App.models import User

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True,widget=forms.TextInput(
    attrs={
    'placeholder':'Email',
    'class':'form-group'
    }))

    password1 = forms.CharField(required=True,widget=forms.PasswordInput(
    attrs={
    'placeholder':'Password',
    'class':'form-group'
    }))
    password2 = forms.CharField(required=True,widget=forms.PasswordInput(
    attrs={
    'placeholder':'Confirm Password',
    'class':'form-group'
    }))


    class Meta:
    	model = User
    	fields = ["email", "password1", "password2"]
