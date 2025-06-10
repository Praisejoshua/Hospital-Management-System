from django.urls import path
from . import views
from .views import (PatientView, MedicalHistoryView, MedicalReportView, 
                    AiAssistantView, InsightsView, DoctorView, HomeView,
                    DoctorAppointmentsView, PatientRecordsView, DoctorNotificationsView,
                    PatientNotificationsView, DoctorInventoryView,
                    PatientRecordsView, PatientDetailView, RandomHealthTipView, ReportAnalyticsView, export_inventory_csv,ApproveMedicalReportView)

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
    path('doctor-inventory-manager/', DoctorInventoryView.as_view(), name='doctor-inventory-manager'),
    # path('analytics-and-reports/', AnalyticsAndReportsView.as_view(), name='analytics-and-reports'),
    path('approve-medical-report/', ApproveMedicalReportView.as_view(), name='approve-medical-report'),
    path('patient-records/', PatientRecordsView.as_view(), name='patient-records'),
    path('patient-records/<int:pk>/', PatientDetailView.as_view(), name='view-patient-records'),
    path('not_authorized/', views.not_authorized, name='not_authorized'),
    path('download-report/<int:appointment_id>/', views.download_report, name='download_report'),
    path('handle-appointment/<int:appointment_id>/<int:accepted_id>/', views.handle_appointment, name='handle_appointment'),
    path('patient-delete-notification/<int:notification_id>/', views.patient_delete_notification, name='patient_delete_notification'),
    path('doctor-delete-notification/<int:notification_id>/', views.doctor_delete_notification, name='doctor_delete_notification'),
    path('random-health-tip/', RandomHealthTipView.as_view(), name='random_health_tip'), # random health tip endpoint
    path('report-analytics/', ReportAnalyticsView.as_view(), name='report_analytics'), # report analytics endpoint
    path('get-answer/', views.get_ai_response, name='get_answer'),
    path('inventory/export/', export_inventory_csv, name='export-inventory'),
]