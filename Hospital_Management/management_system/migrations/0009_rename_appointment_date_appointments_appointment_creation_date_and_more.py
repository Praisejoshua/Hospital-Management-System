# Generated by Django 5.2 on 2025-06-07 15:52

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management_system', '0008_remove_appointments_patient_matric'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointments',
            old_name='appointment_date',
            new_name='appointment_creation_date',
        ),
        migrations.AddField(
            model_name='appointments',
            name='appointment_scheduled_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
