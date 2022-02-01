from django.contrib import admin

# Register your models here.
import users
from users.models import Appointment, Patient
from users.models import Contactus

admin.site.register(Appointment)
admin.site.register(Patient)
admin.site.register(Contactus)
