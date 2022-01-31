from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('', views.homepage, name = "homepage"),
    path('patient/register', views.register, name = 'register'),
    path('patient/login', views.logins, name ='login'),
    path('patient/dashboard', views.dashboard, name = 'dashboard'),
    path('logout', views.logout, name = 'logout'),
    path('set_appointment', views.appointment, name = 'appointment'),
    path('patient/profile',views.profile, name = 'profile'),
    path('contactus', views.contactus, name = 'contactus')

]


