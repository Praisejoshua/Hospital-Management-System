from django.db import models
from django.utils import timezone
from users.models import CustomUser
from django.db import models

class Appointments(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='patient', null=True)
    patient_name = models.CharField(max_length=30)
    patient_matric = models.CharField(max_length=20)
    patient_purpose = models.TextField(max_length=20)
    appointment_date = models.DateTimeField(default=timezone.now)
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
