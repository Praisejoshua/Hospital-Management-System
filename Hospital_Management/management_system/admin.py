from django.contrib import admin
from .models import Appointments, Notification, Inventory


@admin.register(Appointments)
class AssessmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'patient_first_name', 'patient_last_name', 'patient_purpose', 
                    'doctor_selected', 'appointment_creation_date', 'appointment_scheduled_date',
                    'diagnosis', 'doctor_notes', 'prescription', 'doctor_notes', 'status')

@admin.register(Notification)   
class AssessmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')



@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'item_name', 'stock', 'category', 'date_added')
    search_fields = ('item_name', 'category')
    list_filter = ('category',)
    ordering = ('-date_added',)
    date_hierarchy = 'date_added'