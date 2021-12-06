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

def search(request):
    query = request.GET.get('search')
    if len(query) > 75:
        allProps = []
    else:
        allPropsTitle = Property.objects.filter(title__icontains=query)
        allPropsDescription = Property.objects.filter(description__icontains=query)
        allPropsLocation = Property.objects.filter(location__icontains=query)
        allPropsPrice = Property.objects.filter(price__icontains=query)
        allProps = allPropsTitle.union(allPropsDescription, allPropsLocation, allPropsPrice)
    params = {"allProps":allProps, "query":query}
    if len(allProps) > 0:
        return render(request, 'search.html', params)
    else:
        return render(request, 'searchnot.html', params)

def browse(request):
    props = Property.objects.all()
    context = {'props':props}
    return render(request, 'browse.html', context)

def property(request, slug):
    prop = Property.objects.filter(slug=slug).first()
    context = {'prop':prop}
    return render(request, 'property.html', context)