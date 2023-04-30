from django.http.response import HttpResponse
from django.shortcuts import render
from django.db.models import Q
from main.models import Contact, Property, allIps
from django.contrib import messages


def home(request):
    allProps = Property.objects.all().order_by('-views')[:6]

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
    context = {"prop": allProps}

    return render(request, 'index.html', context)


def search(request):
    query = request.GET.get('search')
    if len(query) > 75 or len(query) < 4:
        allProps = []
    else:
        allPropsTitle = Property.objects.filter(title__icontains=query)
        allPropsDescription = Property.objects.filter(description__icontains=query)
        allPropsLocation = Property.objects.filter(location__icontains=query)
        allPropsPrice = Property.objects.filter(price__icontains=query)
        allProps = allPropsTitle.union(allPropsDescription, allPropsLocation, allPropsPrice)
    params = {"allProps": allProps, "query": query}
    if len(allProps) > 0:
        return render(request, 'search.html', params)
    else:
        return render(request, 'searchnot.html', params)


def browse(request):
    props = Property.objects.all()
    context = {'props': props}
    return render(request, 'browse.html', context)


def property(request, slug):
    prop = Property.objects.filter(slug=slug).first()

    def get_client_ip(request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    ip = get_client_ip(request)
    u = allIps(ips=ip, postname=prop.slug)
    result = allIps.objects.filter(Q(ips__icontains=ip) and Q(postname__icontains=prop.slug))
    if len(result) == 1:
        pass
    elif len(result) > 1:
        pass
    else:
        u.save()
        prop.views = prop.views + 1
        prop.save()

    context = {'prop': prop}
    return render(request, 'property.html', context)
