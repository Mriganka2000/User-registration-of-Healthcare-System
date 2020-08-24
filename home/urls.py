from django.contrib import admin
from django.urls import path, include
from home import views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name="contact"),
    path('services', views.services, name="contact"),
    path('faq', views.faq, name="contact"),
    path('team', views.team, name="contact"),
    path('register/', views.register, name="register"),
    path('login/', views.userlogin, name="login"),
    path('logout/', views.userlogout, name="logout"),
]
