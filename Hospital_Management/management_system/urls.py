from django.urls import path
from . import views
from .views import (PatientView, MedicalHistoryView, MedicalReportView, 
                    AiAssistantView, InsightsView, DoctorView, HomeView,
                    DoctorAppointmentsView, PatientRecordsView, DoctorNotificationsView,
                    PatientNotificationsView)

urlpatterns = [
    path('', HomeView.as_view(), name='home-page'),
    path('patient/', PatientView.as_view(), name='patient-dashboard'),
    path('doctor/', DoctorView.as_view(), name='doctor-dashboard'),
    path('doctor-appointments/', DoctorAppointmentsView.as_view(), name='doctor-appointments'),
    path('medical-history/', MedicalHistoryView.as_view(), name='medical-history'),
    path('doctor-notifications/', DoctorNotificationsView.as_view(), name='doctor-notifications'),
    path('medical-notifications/', PatientNotificationsView.as_view(), name='patient-notifications'),
    path('medical-report/', MedicalReportView.as_view(), name='medical-report'),
    path('Ai-assistant/', AiAssistantView.as_view(), name='ai-assistant'),
    path('insights/', InsightsView.as_view(), name='insights'),
    path('patient-records/', PatientRecordsView.as_view(), name='patient-records'),
    path('not_authorized/', views.not_authorized, name='not_authorized'),
    path('handle-appointment/<int:appointment_id>/<int:accepted_id>/', views.handle_appointment, name='handle_appointment'),
    path('patient-delete-notification/<int:notification_id>/', views.patient_delete_notification, name='patient_delete_notification'),
    path('doctor-delete-notification/<int:notification_id>/', views.doctor_delete_notification, name='doctor_delete_notification'),
]
