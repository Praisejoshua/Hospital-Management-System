from django.views.generic import TemplateView
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import AppointmentForm
from .models import Appointments, Notification
from django.http import HttpResponseNotAllowed

class RoleRequiredMixin:
    allowed_roles = []

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if hasattr(request.user, 'role') and request.user.role not in self.allowed_roles:
            return redirect('not_authorized')
        return super().dispatch(request, *args, **kwargs)

class HomeView(TemplateView):
    template_name = 'management_system/home.html'

class PatientView(RoleRequiredMixin, TemplateView):

    template_name = 'management_system/patient-dashboard.html'
    allowed_roles = ['patient']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AppointmentForm()
        context['appointments'] = Appointments.objects.filter(
            user=self.request.user,
            status__in=['accepted']
        ).order_by('-appointment_date')[:3]
        return context

    def post(self, request, *args, **kwargs):
        form = AppointmentForm(request.POST)
        if form.is_valid():
            patient_name = form.cleaned_data['patient_name']
            patient_matric = form.cleaned_data['patient_matric']
            patient_purpose = form.cleaned_data['patient_purpose']
            doctor_selected = form.cleaned_data['doctor_selected']

            Appointments.objects.create(user=request.user,
                                        patient_name=patient_name,
                                        patient_matric=patient_matric,
                                        patient_purpose=patient_purpose,
                                        doctor_selected=doctor_selected)
            messages.success(request, "Appointment Booked Successfully!")
            return self.render_to_response(self.get_context_data(success=True))
        else:
            return self.render_to_response(self.get_context_data(form=form))

class MedicalHistoryView(RoleRequiredMixin, TemplateView):
    template_name = 'management_system/medical-history.html'
    allowed_roles = ['patient']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AppointmentForm()
        context['appointments'] = Appointments.objects.filter(
            user=self.request.user
        ).order_by('-appointment_date')[:10]
        return context

class MedicalReportView(RoleRequiredMixin, TemplateView):
    template_name = 'management_system/medical-report.html'
    allowed_roles = ['patient']

class AiAssistantView(RoleRequiredMixin, TemplateView):
    template_name = 'management_system/AI-assistant.html'
    allowed_roles = ['patient']

class InsightsView(RoleRequiredMixin, TemplateView):
    template_name = 'management_system/insights.html'
    allowed_roles = ['patient']

class PatientNotificationsView(RoleRequiredMixin, TemplateView):
    template_name = 'management_system/patient-notifications.html'
    allowed_roles = ['patient']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['notifications'] = Notification.objects.filter(
            user=self.request.user,
        ).order_by('-date_created')
        return context




# Doctor's view

class DoctorAppointmentsView(RoleRequiredMixin, TemplateView):

    template_name = 'management_system/doctor-appointments.html'
    allowed_roles = ['doctor']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['appointments'] = Appointments.objects.filter(
            doctor_selected=self.request.user,
            status__in=['pending']
        ).order_by('-appointment_date')[:8]
        context['accepted_appointments'] = Appointments.objects.filter(
            doctor_selected=self.request.user,
            status__in=['accepted']
        ).order_by('-appointment_date')[:6]
        return context

@login_required
def not_authorized(request):
    return render(request, 'management_system/not-authorized.html')


# Handle appointment action (accept or reject)
def handle_appointment(request, appointment_id, accepted_id):
    if request.method == 'POST':
        action = request.GET.get('action')
        appointment = get_object_or_404(Appointments, id=appointment_id)
        appointment_date = request.POST.get('appointment_date')

        if appointment_date:
            appointment.appointment_date = appointment_date

        if action == 'accept':
            appointment.status = 'accepted'

            Notification.objects.create(
                user=appointment.user,
                message="The Doctor has accepted your appointment.",
                appointment=appointment
            )
        elif action == 'reject':
            appointment.status = 'rejected'

            Notification.objects.create(
                user=appointment.user,
                message="The Doctor has rejected your appointment.",
                appointment=appointment
            )
        elif action == 'complete':
            appointment.status = 'completed'

            Notification.objects.create(
                user=appointment.user,
                message="The Doctor has ended your appointment.",
                appointment=appointment
            )

        appointment.save()
        return redirect('doctor-appointments')

    return HttpResponseNotAllowed(['POST'])

class DoctorView(RoleRequiredMixin, TemplateView):
    template_name = 'management_system/doctor-dashboard.html'
    allowed_roles = ['doctor']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['appointments'] = Appointments.objects.filter(
            doctor_selected=self.request.user,
            status__in=['accepted']
        ).order_by('-appointment_date')[:5]
        return context
    
class PatientRecordsView(RoleRequiredMixin, TemplateView):
    template_name = 'management_system/patient-records.html'
    allowed_roles = ['doctor']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['appointments'] = Appointments.objects.filter(
            doctor_selected=self.request.user,
            status__in=['completed']
        ).order_by('-appointment_date')[:10]
        return context
    
class DoctorNotificationsView(RoleRequiredMixin, TemplateView):
    template_name = 'management_system/doctor-notifications.html'
    allowed_roles = ['doctor']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['notifications'] = Notification.objects.filter(
            user=self.request.user,
        ).order_by('-date_created')
        return context


def patient_delete_notification(request, notification_id):
    notification = get_object_or_404(Notification, id=notification_id, user=request.user)
    notification.delete()
    return redirect('patient-notifications')

def doctor_delete_notification(request, notification_id):
    notification = get_object_or_404(Notification, id=notification_id, user=request.user)
    notification.delete()
    return redirect('doctorsnotifications')