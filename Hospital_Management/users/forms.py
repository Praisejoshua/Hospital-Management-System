from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        input_formats=['%Y-%m-%d'],
        required=True
    )
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'middle_name', 'last_name',
                  'gender', 'phone', 'date_of_birth', 'blood_group', 'marital_status',
                  'allergies', 'password1', 'password2', 'role'
                ]
