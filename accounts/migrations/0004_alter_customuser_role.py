# Generated by Django 5.0.3 on 2024-04-18 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_department_courses_school_courses_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('teacher', 'Teacher'), ('student', 'Student')], max_length=20),
        ),
    ]
