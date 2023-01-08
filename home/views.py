from django.shortcuts import render , HttpResponse
from datetime import datetime
from home.models import contact

# Create your views here.
def home(request):
    return render(request,'index.html')
def index(request): 
   return render(request, 'index.html')
    # return HttpResponse("this is homepage")

def about(request): 
     return render(request, 'about.html')
    # return HttpResponse("this is about")

def something(request): 
     return render(request, 'something.html')
    # return HttpResponse("this is something")

def contact(request):
    if request.method=="post":
        name= request.POST.get('name')
        email= request.POST.get('email')
        subject= request.POST.get('subject')
        message= request.POST.get('message')
        contact = contact(name=name , email=email , subject =subject , message=message , date=datetime.today())
        contact.save()

    return render(request, 'contact.html')