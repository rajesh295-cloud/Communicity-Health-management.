from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

from django import forms
from django.contrib.auth.models import User

from users.models import Patient


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length= 50)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class ProfileForm(ModelForm):
    class Meta:
        model = Patient
        fields = "__all__"
        exclude = ['user','phone']



class ContactusForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    body = forms.Textarea()



