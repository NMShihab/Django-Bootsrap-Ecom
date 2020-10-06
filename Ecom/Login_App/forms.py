from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from Login_App.models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True,label='',widget=forms.TextInput(
    attrs={
    'placeholder':'Email',
    'class':'form-group'
    }))

    password1 = forms.CharField(required=True,label='',widget=forms.PasswordInput(
    attrs={
    'placeholder':'Password',
    'class':'form-group'
    }))
    password2 = forms.CharField(required=True,label='',widget=forms.PasswordInput(
    attrs={
    'placeholder':'Confirm Password',
    'class':'form-group'
    }))


    class Meta:
    	model = User
    	fields = ["email", "password1", "password2"]


class SignIn(AuthenticationForm):
    email = forms.EmailField(required=True,label='',widget=forms.TextInput(
    attrs={
    'placeholder':'Email',
    'class':'form-group'
    }))
    password = forms.CharField(required=True,label='',widget=forms.PasswordInput(
    attrs={
    'placeholder':'Password',
    'class':'form-group'
    }))
