from django.contrib import admin

# Register your models here.
import patient
from patient.models import Appointment, Patient
from patient.models import Contactus

admin.site.register(Appointment)
admin.site.register(Patient)
admin.site.register(Contactus)
