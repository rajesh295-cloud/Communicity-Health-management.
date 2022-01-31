from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

from . import models


alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
class RegisterForm(UserCreationForm):
    docid = forms.CharField(max_length=50, validators=[alphanumeric])
    full_name = forms.CharField(max_length=255)
    class Meta:
        model = User
        fields = ['full_name','username', 'email', 'password1', 'password2']




class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)



