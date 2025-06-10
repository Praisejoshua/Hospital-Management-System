from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'Users/home.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account successfully created!")
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'users/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                if user.role == 'doctor':
                    messages.success(request, "Welcome!")
                    return redirect('doctor-dashboard')
                elif user.role == 'patient':
                    messages.success(request, "Welcome!")
                    return redirect('patient-dashboard')
                else:
                    return redirect('default_dashboard')
            else:
                return redirect('login')
    else:
        form = AuthenticationForm()
        
    return render(request, 'users/login.html', {'form': form})

@login_required
def patient_profile(request):
    if request.user.role != 'patient':
        return redirect('not_authorized')
    
    if request.method == 'POST':
        request.user.first_name = request.POST.get('first_name')
        request.user.last_name = request.POST.get('last_name')
        request.user.email = request.POST.get('email')
        request.user.middle_name = request.POST.get('middle_name')
        request.user.gender = request.POST.get('gender')
        request.user.dob = request.POST.get('dob')
        request.user.blood_group = request.POST.get('blood_group')
        request.user.marital_status = request.POST.get('marital_status')
        request.user.phone = request.POST.get('phone')
        request.user.allergies = request.POST.get('allergies')
        request.user.sponsor_full_name = request.POST.get('sponsor_full_name')
        request.user.sponsor_email = request.POST.get('sponsor_email')
        request.user.sponsor_phone = request.POST.get('sponsor_phone')
        request.user.sponsor_relation = request.POST.get('sponsor_relation')

        request.user.save()

        messages.success(request, "Profile updated successfully!")
        return redirect('patient-profile')

    return render(request, 'users/patient-profile.html')

@login_required
def doctor_profile(request):
    if request.user.role != 'doctor':
        return redirect('not_authorized')

    # Handle profile info update
    if request.method == 'POST':
        request.user.first_name = request.POST.get('first_name')
        request.user.last_name = request.POST.get('last_name')
        request.user.email = request.POST.get('email')
        request.user.middle_name = request.POST.get('middle_name')
        request.user.gender = request.POST.get('gender')
        request.user.dob = request.POST.get('dob')
        request.user.blood_group = request.POST.get('blood_group')
        request.user.marital_status = request.POST.get('marital_status')
        request.user.phone = request.POST.get('phone')
        request.user.save()

        messages.success(request, "Profile updated successfully!")
        return redirect('doctor-profile')

    return render(request, 'users/doctor-profile.html')



