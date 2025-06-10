from django.contrib import admin
from django.contrib.auth import views as auth_views 
from django.urls import path, include
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('login/', user_views.user_login, name='login'),
    path('doctor-profile/', user_views.doctor_profile, name='doctor-profile'),
    path('patient-profile/', user_views.patient_profile, name='patient-profile'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('', include('management_system.urls')),
]
