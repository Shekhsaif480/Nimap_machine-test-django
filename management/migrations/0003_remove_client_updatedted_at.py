# Generated by Django 5.1.5 on 2025-01-20 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0002_client_updatedted_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='updatedted_at',
        ),
    ]
