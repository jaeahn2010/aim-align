# Generated by Django 5.0.1 on 2024-03-22 22:57

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_goal_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='start_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
