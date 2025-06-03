from django.contrib import admin
from .models import Appointments, Notification


@admin.register(Appointments)
class AssessmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'patient_name', 'patient_matric',
                    'patient_purpose', 'doctor_selected', 'appointment_date', 'status')

@admin.register(Notification)   
class AssessmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')
