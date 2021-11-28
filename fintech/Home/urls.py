from django.contrib import admin
from django.urls import path
from Home import views

urlpatterns = [
    path("", views.index, name= 'Home'),
    path("contact", views.contact, name= 'contact'),
    path("login", views.login, name= 'login'),
    path("signup", views.signup, name= 'signup'),
    path("photo", views.photo, name= 'photo'),
    path("addvoice", views.addvoice, name= 'addvoice'),
]
