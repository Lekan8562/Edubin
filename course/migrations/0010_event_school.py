# Generated by Django 5.0.3 on 2024-04-21 18:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_alter_customuser_role'),
        ('course', '0009_remove_quiz_course_quiz_topic'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='school',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='school_events', to='accounts.school'),
        ),
    ]
