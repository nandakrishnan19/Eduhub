# Generated by Django 4.1.7 on 2023-03-29 04:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_faculty_fnumber_hod_hdepartment_hod_hnumber_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='rollno',
        ),
    ]