from django.shortcuts import render,HttpResponse
from datetime import datetime
from Myapp.models import Login
from django.contrib import messages
def index(request):
    context={
        'variable':'this is sent'
    }   
    return render(request,'index.html',context)
   # return HttpResponse("This is Homepage")

# Create your views here.
def about(request):
    return render(request,'about.html')

    #return HttpResponse("This is about us Page")

def services(request):
    return render(request,'services.html')

    #return HttpResponse("This is services Page")

def contact(request):
    return render(request,'contact.html')

def login(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        login=Login(name='name',email='email',phone='phone',desc='desc',date=datetime.today())
        login.save()
        messages.success(request, "Your message has been sent")
    return render(request,'login.html')

   # return HttpResponse("This is contact us Page")
