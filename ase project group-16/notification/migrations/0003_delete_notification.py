# Generated by Django 3.0.2 on 2020-03-14 14:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0002_notification_curr_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Notification',
        ),
    ]
