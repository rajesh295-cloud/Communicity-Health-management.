# Generated by Django 3.2.9 on 2022-01-19 06:03

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('patient', '0003_appointment'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Profile',
            new_name='Patient',
        ),
    ]