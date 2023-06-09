# Generated by Django 4.1.7 on 2023-04-26 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_acceptedhod_alter_acceptedfaculty_ffaculty_cpassword_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='acceptedhod',
            old_name='hdepartment',
            new_name='hhdepartment',
        ),
        migrations.RenameField(
            model_name='acceptedhod',
            old_name='hemail',
            new_name='hhemail',
        ),
        migrations.RenameField(
            model_name='acceptedhod',
            old_name='hod_cpassword',
            new_name='hhname',
        ),
        migrations.RenameField(
            model_name='acceptedhod',
            old_name='hname',
            new_name='hhnumber',
        ),
        migrations.RenameField(
            model_name='acceptedhod',
            old_name='hpassword',
            new_name='hhod_cpassword',
        ),
        migrations.RemoveField(
            model_name='acceptedhod',
            name='hnumber',
        ),
        migrations.AddField(
            model_name='acceptedhod',
            name='hhpassword',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hod',
            name='hnumber',
            field=models.CharField(max_length=100),
        ),
    ]
