# Generated by Django 5.0.3 on 2024-04-21 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_alter_customuser_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('teacher', 'Teacher'), ('student', 'Student')], max_length=20),
        ),
    ]
