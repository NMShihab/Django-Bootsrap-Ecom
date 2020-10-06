from django.shortcuts import render
from .forms import SignUpForm,SignIn
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.shortcuts import HttpResponseRedirect
from django.http import  HttpResponse
from django.urls import  reverse


# Create your views here.


# Sign Up views

def signup(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form':form}

    return render(request,'Login_App/Signup.html',context)


# Login View
def login_(request):
    form = AuthenticationForm()

    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username,password=password)

            if user is not None:
                login(request,user)
                return HttpResponse("logged in")

    return render(request,'Login_App/Login.html',context={'form':form})
