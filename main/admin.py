from django.contrib import admin
from main.models import Contact, Property, allIps

# Register your models here.
admin.site.register(Contact)
admin.site.register(Property)
admin.site.register(allIps)