# Generated by Django 4.1.7 on 2023-04-01 10:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_acceptedstudent_semester'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='absent',
        ),
        migrations.RemoveField(
            model_name='student',
            name='percentage',
        ),
        migrations.RemoveField(
            model_name='student',
            name='present',
        ),
    ]
