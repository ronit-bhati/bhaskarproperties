from django.http.response import HttpResponse
from django.shortcuts import render
from main.models import Contact, Property
from django.contrib import messages

def home(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        messege = request.POST['messege']

        if len(name) < 3 or len(email) < 8 or len(phone) < 10 or len(messege) < 5:
            messages.warning(request, "Please fill the form correctly!")

        else:
            contact = Contact(name=name, email=email, phone=phone, messege=messege)
            contact.save()
            messages.success(request, "Your form has been submitted!")

    return render(request, 'index.html')

def browse(request):
    return render(request, 'browse.html')

def property(request, slug):
    return render(request, 'property.html')