# Generated by Django 5.0.1 on 2024-03-26 19:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_alter_checkpoint_end_date_alter_checkpoint_status_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='checkpoint',
            old_name='status',
            new_name='is_complete',
        ),
        migrations.RenameField(
            model_name='goal',
            old_name='status',
            new_name='is_complete',
        ),
    ]