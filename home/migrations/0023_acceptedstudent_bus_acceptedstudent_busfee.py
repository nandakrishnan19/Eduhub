# Generated by Django 4.1.7 on 2023-05-03 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_bus'),
    ]

    operations = [
        migrations.AddField(
            model_name='acceptedstudent',
            name='bus',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='acceptedstudent',
            name='busfee',
            field=models.IntegerField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
