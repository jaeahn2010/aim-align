# Generated by Django 5.0.1 on 2024-03-23 03:55

import datetime
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_goal_status_checkpoint'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='checkpoint',
            options={'ordering': ['end_date']},
        ),
        migrations.AlterField(
            model_name='checkpoint',
            name='end_date',
            field=models.DateField(default=datetime.date(2024, 3, 24), verbose_name='checkpoint end date'),
        ),
        migrations.AlterField(
            model_name='checkpoint',
            name='start_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='checkpoint start date'),
        ),
        migrations.AlterField(
            model_name='goal',
            name='end_date',
            field=models.DateField(default=datetime.date(2024, 3, 24)),
        ),
    ]
