from django import forms
from users.models import CustomUser
from .models import Inventory

class AppointmentForm(forms.Form):
    doctor_selected = forms.ModelChoiceField(
        queryset=CustomUser.objects.filter(role='doctor'),
        empty_label="Select Doctor",
        label="Choose Doctor",
        widget=forms.Select(attrs={
            'class': 'form-control',
            'style': 'width: 100%; padding: 8px; border-radius: 6px;'
            })
    )
    patient_purpose = forms.CharField(
        max_length=20,
        widget=forms.Textarea(attrs={
            'rows': 5,
            'cols': 40
        }),
        label="Purpose of Appointment"
    )

class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = [
            "item_name",
            "stock",
            "category",
            "date_added",
        ]
        widgets = {
            "date_added": forms.DateInput(attrs={"type": "date"})
        }
 