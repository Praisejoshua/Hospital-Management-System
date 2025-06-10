from django.db import models
from django.utils import timezone
from users.models import CustomUser
from django.db import models

class Appointments(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='patient', null=True)
    patient_first_name = models.CharField(max_length=30, default='null')
    patient_last_name = models.CharField(max_length=30, default='null')
    patient_purpose = models.TextField(max_length=20)
    appointment_creation_date = models.DateTimeField(default=timezone.now)
    appointment_scheduled_date = models.DateTimeField(default=timezone.now)
    doctor_selected = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'doctor'},
        related_name='selected_doctor', null=True
    )
    STATUS_CHOICES = [
    ('pending', 'Pending'),
    ('accepted', 'Accepted'),
    ('rejected', 'Rejected'),
    ('completed', 'Completed'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    diagnosis = models.TextField(max_length=20, null=True)
    doctor_notes = models.TextField(max_length=50, null=True)
    prescription = models.TextField(max_length=50, null=True)
    doctor_result = models.TextField(max_length=30, null=True)

class Notification(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='notifications')
    appointment = models.ForeignKey(Appointments, on_delete=models.CASCADE, null=True, blank=True)
    message = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)


class Inventory(models.Model):
    item_name = models.CharField(max_length=100)
    stock = models.CharField()
    category = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)  # not in form
    date_added = models.DateField(null=True, blank=True)    # editable field

    def __str__(self):
        return self.item_name