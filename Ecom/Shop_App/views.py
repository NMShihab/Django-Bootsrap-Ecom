from django.shortcuts import render
from django.views.generic import ListView

from Shop_App.models import Product
# Create your views here.

 # def home(request):
 #
 #    return render(request,'Shop_App/Home.html')


class Home(ListView):
    model = Product
    template_name = 'Shop_App/Home.html'

def contact(request):

    return render(request,'Shop_App/contact.html')
