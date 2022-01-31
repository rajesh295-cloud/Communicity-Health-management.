from django.contrib import messages
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
# Create your views here.
from doctors.forms import RegisterForm,  LoginForm
from doctors.models import Doctor


def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'], password=data['password'])
            print(user)
            if user is not None:
                if user.is_staff:
                    auth_login(request, user)
                    return redirect('/admin')
                elif not user.is_staff:
                    auth_login(request, user)
                    return redirect('/doctors/waitdoctor')
            else:
                messages.add_message(request, messages.ERROR, "Invalid user credentials")
                return render(request, 'doctors/doctorlogin.html', {'form_login': form})
    context = {
        'form_login': LoginForm,
        'activate_login': 'active'
    }
    return render(request, 'doctors/doctorlogin.html')



def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            Doctor.objects.create(user = user, username = user.username)

            return redirect('/doctors/doctorlogin')
    context = {'form':form}
    return render(request, 'doctors/signupdoctor.html', context)


def waitdoc(request):

    return render(request, 'doctors/waitdoctor.html')