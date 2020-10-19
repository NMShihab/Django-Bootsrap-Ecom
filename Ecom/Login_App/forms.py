from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from Login_App.models import User, UserProfile


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

class Profile_form(forms.ModelForm):
    username = forms.CharField(label='',widget = forms.TextInput(
    attrs={
    'placeholder':'Username',
    'class':'form-profile',
    }))

    full_name = forms.CharField(label='',widget = forms.TextInput(
    attrs={
    'placeholder':'Full Name',
    'class':'form-profile',
    }))

    city = forms.CharField(label='',widget = forms.TextInput(
    attrs={
    'placeholder':'City',
    'class':'form-profile',
    }))
    country = forms.CharField(label='',widget = forms.TextInput(
    attrs={
    'placeholder':'Country',
    'class':'form-profile',
    }))

    zipcode = forms.CharField(label='',widget = forms.TextInput(
    attrs={
    'placeholder':'Zip Code',
    'class':'form-profile',
    }))

    phone = forms.CharField(label='',widget = forms.TextInput(
    attrs={
    'placeholder':'Phone Number',
    'class':'form-profile',
    }))
    address = forms.CharField(label='',widget = forms.Textarea(
    attrs={
    'placeholder':'Type Proper Address',
    'class':'form-profile',
    }))

    class Meta:
        model = UserProfile
        fields = ["username", "full_name", "city","country","zipcode","phone","address"]
