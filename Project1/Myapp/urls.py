from django.contrib import admin
from django.urls import path
from Myapp import views
urlpatterns = [
    path("",views.index, name='Home'),
    path("about",views.about, name='about'),
    path("services",views.services, name='services'),
    path("contact",views.contact, name='contact'),
    path("login",views.login,name='login'),

]