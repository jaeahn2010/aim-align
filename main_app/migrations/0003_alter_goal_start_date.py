# Generated by Django 5.0.1 on 2024-03-22 22:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_goal_end_date_goal_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2024, 3, 22, 22, 57, 35, 798960, tzinfo=datetime.timezone.utc)),
        ),
    ]
