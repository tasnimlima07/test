from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Contract

def dashboard(request):
   return render(request, 'home.html')

def home(request):
   return render(request, 'home.html')
   

def blog(request):
   return render(request, 'blog.html')


def about(request):
   return render(request, 'about.html')

from django.shortcuts import render
from django.http import HttpResponse
from .models import Contract  # Assuming you have a Contract model defined

def contract(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        des = request.POST['des']
        values = Contract(name=name, email=email, des=des)
        values.save()
    
    return render(request, 'contract.html')

