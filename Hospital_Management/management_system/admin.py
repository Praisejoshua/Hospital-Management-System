from django.contrib import admin
from .models import Appointments


@admin.register(Appointments)
class AssessmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'patient_name', 'patient_matric',
                    'patient_purpose', 'doctor_selected', 'appointment_date', 'status')
