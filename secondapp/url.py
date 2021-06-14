from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('about',views.about, name='about'),
    path('services',views.services, name='services'),
    path('contact',views.contact, name='contact'),
    path('form',views.form, name='form'),
    path("checkout", views.checkout, name="Checkout"),
    path("handlerequest", views.handlerequest, name="handlerequest"),
    
]