from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.shortcuts import render, redirect

from users.forms import RegisterForm, LoginForm, ProfileForm
from django.contrib import messages, auth

from users.auth import unauthenticated_user,  admin_only, user_only
from users.models import  Appointment, Patient


def homepage(request):
    return render(request, 'homepage.html')



@unauthenticated_user
def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            Patient.objects.create(user = user, username = user.username, email = user.email)

            return redirect('login')
    context = {'form':form}
    return render(request, 'users/registration.html', context)






def contactus(request):
    return render(request, 'contactus.html')


def gallery(request):
    return render(request, 'gallery.html')



@unauthenticated_user
def logins(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'], password=data['password'])
            print(user)
            if user is not None:
                if user.is_staff:
                    login(request, user)
                    return redirect('/admin')
                elif not user.is_staff:
                    login(request, user)
                    return redirect('/users/dashboard')
            else:
                messages.add_message(request, messages.ERROR, "Invalid user credentials")
                return render(request, 'users/login.html', {'form_login': form})
    context = {
        'form_login': LoginForm,
        'activate_login': 'active'
    }
    return render(request, 'users/login.html', context)


def dashboard(request):

    return render(request, 'users/dashboard.html')


def logout(request):
    auth.logout(request)
    return redirect("/users/login")


def appointment(request):
    if request.method == "POST":
        your_name = request.POST['your-name']
        your_phone = request.POST['your-phone']
        your_email = request.POST['your-email']
        your_address = request.POST['your-address']
        your_schedule = request.POST['your-schedule']
        your_date = request.POST['your-date']
        your_message = request.POST['your-message']


        appointment = "Name: " + your_name + " Phone: " + your_phone + " Email: " + your_email + " Address: " + your_address + " Schedule: " + your_schedule + " Day: " + your_date + " Message: " + your_message

        Appointment.objects.create(your_name = your_name, your_phone = your_phone, your_email = your_email, your_address = your_address)
        return render(request, 'appointment_confirmation.html', {
            'your_name': your_name,
            'your_phone': your_phone,
            'your_email': your_email,
            'your_address': your_address,
            'your_schedule': your_schedule,
            'your_date': your_date,
            'your_message': your_message
        })

    else:
        return render(request, 'set_appointment.html', {})


def profile(request):
    profile = request.user.profile
    form = ProfileForm(instance=Profile)
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance =profile)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS,"Account Updated Successfully")
            return redirect('profile')
    context = {'form': form}
    return render(request,'users/profile.html',context)


