from django.urls import path
from . import views
from .views import (PatientView, MedicalHistoryView, MedicalReportView, 
                    AiAssistantView, InsightsView, DoctorView, HomeView,
                    DoctorAppointmentsView)

urlpatterns = [
    path('', HomeView.as_view(), name='home-page'),
    path('patient/', PatientView.as_view(), name='patient-dashboard'),
    path('doctor/', DoctorView.as_view(), name='doctor-dashboard'),
    path('doctor-appointments/', DoctorAppointmentsView.as_view(), name='doctor-appointments'),
    path('medical-history/', MedicalHistoryView.as_view(), name='medical-history'),
    path('medical-report/', MedicalReportView.as_view(), name='medical-report'),
    path('Ai-assistant/', AiAssistantView.as_view(), name='ai-assistant'),
    path('insights/', InsightsView.as_view(), name='insights'),
    path('not_authorized/', views.not_authorized, name='not_authorized'),
    path('handle-appointment/<int:appointment_id>/<int:accepted_id>/', views.handle_appointment, name='handle_appointment'),

]