# Generated by Django 5.0.7 on 2024-11-12 06:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planit', '0007_applicationchangehistory_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applicationchangehistory',
            name='previous_status',
        ),
    ]
