from django.shortcuts import render


# Create your views here.


# Sign Up views

def signup(request):

    return render(request,'Login_App/Signup.html')


# Login View
def login(request):

    return render(request,'Login_App/Login.html')
