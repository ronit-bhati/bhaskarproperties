from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search', views.search, name='search'),
    path('browse', views.browse, name='browse'),
    path('property/<str:slug>', views.property, name='property'),
]
