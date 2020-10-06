from django.shortcuts import render

# Create your views here.

def home(request):

    return render(request,'Shop_App/Home.html')



def contact(request):

    return render(request,'Shop_App/contact.html')
