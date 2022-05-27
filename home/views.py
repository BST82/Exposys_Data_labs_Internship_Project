from multiprocessing import context
from datetime import datetime
from urllib import request
from home.models import Contact
from django.contrib import messages

from django.shortcuts import redirect, render, HttpResponse


# Create your views here.

def index(request):
    return render(request,'index.html')

    # context = {
    #     'variable1':"this is send1",
    #     'variable2':"this is send2",
    # }
    #return render(request,'index.html',context)
   # return HttpResponse("This is home page")

# def home(request):
#     return render(request,'home.html') 

def meabout(request):
    return render(request,'meabout.html')
    #return HttpResponse("This is about page")

def projects(request):
    return render(request,'projects.html')
    #return HttpResponse("This is projects page")
    
def skill(request):
    return render(request,'skill.html')

def certificates(request):
    return render(request,'certificates.html')

def social(request):
    return render(request,'social.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, 'Your massage has been sent!')
        return redirect('index')
    return render(request,'contact.html')

    #return HttpResponse("This is contact page")
    
def style(request):
    return render(request,'base.html')












