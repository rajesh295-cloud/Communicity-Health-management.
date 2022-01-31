from django.db import models

# Create your models here.

class Bookings(models.Model):
    your_name = models.CharField(max_length=50)
    your_phone = models.CharField(max_length=10)
    your_email = models.EmailField(null=True)
    your_address = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.your_name} Booking'