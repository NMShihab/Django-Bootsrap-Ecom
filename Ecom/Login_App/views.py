from django.shortcuts import render
from .forms import SignUpForm


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
def login(request):

    return render(request,'Login_App/Login.html')
