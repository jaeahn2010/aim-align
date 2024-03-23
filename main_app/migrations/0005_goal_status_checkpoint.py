# Generated by Django 5.0.1 on 2024-03-22 23:12

import datetime
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_alter_goal_start_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='goal',
            name='status',
            field=models.CharField(choices=[('C', 'Complete'), ('I', 'Incomplete')], default='I', max_length=1),
        ),
        migrations.CreateModel(
            name='Checkpoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=250)),
                ('start_date', models.DateField(default=django.utils.timezone.now)),
                ('end_date', models.DateField(default=datetime.date(2024, 3, 23))),
                ('status', models.CharField(choices=[('C', 'Complete'), ('I', 'Incomplete')], default='I', max_length=1)),
                ('goal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.goal')),
            ],
        ),
    ]
