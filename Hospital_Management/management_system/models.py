from django.db import models
from django.utils import timezone
from users.models import CustomUser

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