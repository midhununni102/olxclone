# Generated by Django 4.1.2 on 2023-01-16 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('olx', '0002_alter_notifications_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notifications',
            name='status',
            field=models.CharField(choices=[('sent', 'sent'), ('pending', 'pending'), ('cancelled', 'cancelled')], max_length=50),
        ),
    ]