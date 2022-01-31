from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('doctors/doctorlogin', views.login, name = 'doctorlogin'),
    path('doctors/doctorsignup', views.register, name = 'doctorsignup'),
    path('doctors/waitdoctor', views.waitdoc, name = 'waitdoc')
]
