# Generated by Django 5.2 on 2025-06-03 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_alter_customuser_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_picture',
            field=models.ImageField(blank=True, default='profile_pics/default_pic.jpg', null=True, upload_to='profile_pics/'),
        ),
    ]
