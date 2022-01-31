from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.forms import PasswordInput




class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null = True)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=10)



    def __str__(self):
        return f'{self.user.username} Profile'


    @property
    def get_id(self):
        return self.user.id



class Appointment(models.Model):
    your_name = models.CharField(max_length = 50)
    your_phone = models.CharField(max_length= 10)
    your_email = models.EmailField(null = True)
    your_address = models.CharField(max_length= 50)


    def __str__(self):
        return f'{self.your_name} Appointment'




class Contactus(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
