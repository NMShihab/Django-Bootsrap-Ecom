from django.shortcuts import render
from .forms import SignUpForm,SignIn,Profile_form
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.shortcuts import HttpResponseRedirect
from django.http import  HttpResponse
from django.urls import  reverse
from django.contrib.auth.decorators import login_required
from Login_App.models import UserProfile


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
    #form = SignIn()

    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            username= form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username,password=password)

            if user is not None:
                login(request,user)
                return HttpResponseRedirect(reverse("Shop_App:home"))

    return render(request,'Login_App/Login.html',context={'form':form})

@login_required
def logOut(request):
    logout(request)
    # messages.warning(request, "You are logged out!!")
    return HttpResponseRedirect(reverse('Shop_App:home'))

@login_required
def edit_profile(request):
    current_user = UserProfile.objects.get(user = request.user)
    form = Profile_form(instance=current_user)

    if request.method == "POST":
        form = Profile_form(data = request.POST,instance=current_user)

        if form.is_valid():
            form.save()
            # messages.success(request,"Your profile updated")
            form = Profile_form(instance=current_user)

    return render(request,"Login_App/profile.html",context={'form':form})
