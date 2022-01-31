from django.contrib import admin
from django.urls import path, include

from bookings import views

urlpatterns = [
    path('book', views.book, name = "book")

]
