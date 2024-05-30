from django.shortcuts import render, HttpResponse
from datetime import datetime
from dreamplayapp.models import Contact

# Create your views here.

def index(request):
    return render(request, 'index.html')

def vr(request):
    return render(request, 'vr.html')

def kz(request):
    return render(request, 'kz.html')

def gallery(request):
    return render(request, 'gallery.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        about=request.POST.get('about')
        contact=Contact(name=name, phone=phone, email=email, about=about, date=datetime.today())
        contact.save()
    return render(request, 'contact.html')
