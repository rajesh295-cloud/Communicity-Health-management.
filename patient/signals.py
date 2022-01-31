from django.db.models.signals import post_save, pre_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Patient

@receiver(post_save, sender = User)
def create_profile(sender, instance, created, **kwargs):
    return 1