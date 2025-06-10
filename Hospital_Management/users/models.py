from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('doctor', 'Doctor'),
        ('patient', 'Patient'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='patient')
    profile_picture = models.ImageField(
        upload_to='profile_pics/',
        default='profile_pics/default_pic.jpg',
        blank=True,
        null=True
    )
    first_name = models.CharField(max_length=30, blank=True, null=True)
    middle_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(max_length=30, blank=True, null=True)
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    gender = models.CharField(
        max_length=20,
        choices=GENDER_CHOICES,
        blank=True,
        null=True
    )
    phone = models.CharField(max_length=15, blank=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    BLOOD_GROUP_CHOICES = [
        ('AA', 'AA'),
        ('AS', 'AS'),
        ('SS', 'SS'),
    ]
    blood_group = models.CharField(
        max_length=5,
        choices=BLOOD_GROUP_CHOICES,
        blank=True,
        null=True
    )
    MARITAL_STATUS_CHOICES = [
        ('Single', 'Single'),
        ('Married', 'Married'),
        ('Divorced', 'Divorced'),
    ]
    marital_status = models.CharField(
        max_length=20,
        choices=MARITAL_STATUS_CHOICES,
        blank=True,
        null=True
    )
    ALLERGIES_CHOICES = [
        ('none', 'None'),
        ('nuts', 'Nuts'),
        ('egg', 'Egg'),
        ('milk', 'Milk'),
        ('fish', 'Fish'),
    ]
    allergies = models.CharField(
        max_length=20,
        choices=ALLERGIES_CHOICES,
        blank=True,
        null=True
    )
    sponsor_full_name = models.CharField(max_length=30, blank=True, null=True)
    sponsor_email = models.EmailField(max_length=30, blank=True, null=True)
    sponsor_phone = models.CharField(max_length=15, blank=True, null=True)
    RELATIONS_CHOICES = [
        ('father', 'Father'),
        ('mother', 'Mother'),
        ('aunt', 'Aunt'),
        ('uncle', 'Uncle'),
        ('next-of-kin', 'Next of Kin'),
        ('guardian', 'Guardian'),
    ]
    sponsor_relation = models.CharField(
        max_length=20,
        choices=RELATIONS_CHOICES,
        blank=True,
        null=True
    )
